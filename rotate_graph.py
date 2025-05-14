"""
les fuckin gooooooooo
"""

import numpy as np
import manim as ma  # type: ignore  # pylint: disable=E0401


class RotateGraph(ma.ThreeDScene):
    """
    mentoría de calculo go brrrrr
    """

    def construct(self):
        """
        anima la revolución (rise up) de una gráfica
        """

        axes = ma.ThreeDAxes(
            x_range=[0, 8, 1],
            y_range=[-8, 8, 1],
            z_range=[-8, 8, 1],
        )

        self.move_camera(zoom=0.6)
        func = axes.plot(lambda x: 0.1 * (x**2), color=ma.YELLOW, x_range=[1, 6])
        func.set_stroke(width=5)
        area = axes.get_area(func, x_range=[1, 6], color=ma.BLUE, opacity=0.6)
        graph = ma.VGroup(func, area)

        solid = ma.Surface(
            lambda u, v: axes.c2p(
                u, 0.1 * (u**2) * np.cos(v), 0.1 * (u**2) * np.sin(v)
            ),
            u_range=[0, 6],
            v_range=[0, 2 * ma.PI],
            resolution=16,
        )

        self.play(ma.Create(axes), run_time=2)
        self.play(ma.Create(func), run_time=2)
        self.play(ma.Create(area), run_time=2)
        self.move_camera(phi=ma.PI / 3, theta=-ma.PI / 4, zoom=0.6, run_time=4)
        self.begin_ambient_camera_rotation(0.2)
        self.wait(1)
        self.play(
            ma.Rotate(
                mobject=graph,
                angle=4 * ma.PI,
                about_point=ma.ORIGIN,
                axis=ma.X_AXIS,
            ),
            run_time=8,
            rate_func=ma.smoothstep,
        )

        self.play(ma.FadeIn(solid, target_position=axes))
        self.move_camera(theta=-ma.PI / 4, run_time=8)
        self.stop_ambient_camera_rotation()
        self.play(
            ma.Rotate(
                mobject=graph,
                angle=4 * ma.PI,
                about_point=ma.ORIGIN,
                axis=ma.X_AXIS,
            ),
            run_time=8,
            rate_func=ma.smoothstep,
        )

        self.wait(5)
