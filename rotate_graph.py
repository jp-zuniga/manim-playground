"""
les fuckin gooooooooo
"""

import numpy as np
import manim as ma  # type: ignore


class RotateGraph(ma.ThreeDScene):
    """
    mentoría de calculo go brrrrr
    """

    def construct(self):
        """
        animar la revolución (rise up) de una gráfica
        """

        ax = ma.ThreeDAxes(
            x_range=[0, 10, 1],
            y_range=[-10, 10, 1],
            z_range=[-10, 10, 1],
        )

        ax.move_to(ma.ORIGIN)

        function = ax.plot(lambda x: x**2, color=ma.YELLOW, x_range=[0, 4])
        function.set_stroke(width=5)
        area = ax.get_area(function, x_range=[0, 3], color=ma.BLUE, opacity=0.6)

        graph = ma.VGroup(function, area)

        self.play(ma.Create(ax), run_time=2)
        self.play(ma.Create(function), run_time=2)
        self.play(ma.Create(area), run_time=2)
        self.move_camera(phi=ma.PI / 3, theta=-ma.PI / 4, run_time=4)
        self.begin_ambient_camera_rotation(0.2)
        self.wait(1)
        self.play(
            ma.Rotate(
                mobject=graph,
                angle=8 * ma.PI,
                about_point=ma.ORIGIN,
                axis=ma.X_AXIS,
            ),
            run_time=12,
            rate_func=ma.smoothstep,
        )

        solid = ma.Surface(
            lambda u, v: np.array([u**2, u * np.cos(v), u * np.sin(v)]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=16,
        )

        solid.move_to(ax)
        self.play(
            (
                ma.FadeOut(graph, scale=0.5, target_position=ax),
                ma.FadeIn(solid, scale=1.5),
            ),
            run_time=3,
        )

        self.move_camera(phi=3*ma.PI / 4, zoom=0.8, run_time=4)
        self.wait(2)
        self.move_camera(phi=-ma.PI / 4, run_time=6)
        self.wait(6)
