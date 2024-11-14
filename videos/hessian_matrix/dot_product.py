from manim import *
import numpy as np

class VectorExample(Scene):
    def construct(self):
        M=np.array([[2,3],[0,2]])
        m_matrix = Matrix(M)
        tex_H = Tex(r"$H = $", color=WHITE)
        matrix_group = VGroup(tex_H, m_matrix).arrange(RIGHT).to_corner(UL)
        self.play(Write(m_matrix), Write(tex_H))
        vec_np=np.array([1,1])
        new_vec_np=M@vec_np
        vec=Vector(vec_np,color=GREEN)
        tex_delta_s = Tex(r"$\Delta \vec{s}$", color=GREEN).next_to(vec.get_end(), RIGHT)
        new_vec=Vector(new_vec_np)
        tex_H_delta_s = Tex(r"$H \Delta \vec{s}$", color=WHITE).next_to(new_vec.get_end(), RIGHT)
        angle=Angle(vec,new_vec,other_angle=True)
        self.add(vec,tex_delta_s)
        self.wait(2)
        self.add(new_vec,tex_H_delta_s)
        self.play(TransformFromCopy(vec, new_vec))
        self.play(FadeIn(angle))
        dot_product = np.dot(new_vec_np, vec_np)
        dot_product_tex = MathTex(r"\Delta \vec{s} \cdot H \Delta \vec{s} =", color=WHITE).to_corner(LEFT)
        dot_product_tex[0][0:3].set_fill(color=GREEN)
        self.play(Write(dot_product_tex))
        dot_product_value = MathTex(f"{dot_product:.2f}", color=YELLOW).next_to(dot_product_tex, RIGHT)
        self.play(Write(dot_product_value))
        self.interactive_embed()
        