from manim import *
import numpy as np
import sympy as sp
from sympy.abc import x

def taylor_series(function: callable, x0: float, degree: int):
    taylor = sp.series(function, x, x0=x0, n=degree+1).removeO()
    coefs = [taylor.coeff(x, i) for i in range(degree+1)]
    return np.polynomial.Polynomial(coefs)

class TaylorSeriesVisualization(Scene):
    def construct(self):
        function = sp.sin(x)
        x0 = 0
        max_degree = 10
        axes = Axes(
            x_range=[-2 * np.pi, 2 * np.pi, np.pi / 2],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"color": BLUE}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        
        self.play(Create(axes), Write(axes_labels))

        original_function = axes.plot(
            sp.lambdify(x,function,"numpy"),
            color=RED,
            x_range=[-2 * np.pi, 2 * np.pi]
        )
        self.play(Create(original_function))
        taylor_poly = taylor_series(function, x0, 1)

        taylor_function = axes.plot(
                lambda t: taylor_poly(t),
                color=GREEN,
                x_range=[-2 * np.pi, 2 * np.pi]
            )
        taylor_label = Text(f"{str(taylor_poly)}").to_corner()
        self.play(Create(taylor_function), Write(taylor_label))
        for degree in range(3, max_degree + 1,2):
            new_taylor_poly = taylor_series(function, x0, degree)
            new_taylor_function = axes.plot(
                lambda t: new_taylor_poly(t),
                color=GREEN,
                x_range=[-2 * np.pi, 2 * np.pi]
            )
            new_taylor_label = Text(f"{str(new_taylor_poly)}").to_corner()
            self.play(Transform(taylor_function,new_taylor_function), 
                     Transform(taylor_label,new_taylor_label))
            self.wait(1)
        self.wait(2)
