from manim import *
import numpy as np

np.random.seed(42)

SQUARE_COLOR = BLUE_E
DOT_COLOR = RED
HIGHLIGHT_COLOR = YELLOW
CROSSHAIR_COLOR = YELLOW


class ContinuousSampleSpace(Scene):
    """Visualizes a continuous sample space: dart thrown at a unit square."""

    def construct(self):
        # --- Title card ---
        title = Text("Continuous Sample Space", font_size=44)
        subtitle = Text("Dart thrown at a unit square", font_size=26, color=GREY)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(title), FadeIn(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

        # --- Setup: unit square with axes ---
        axes = Axes(
            x_range=[0, 1.1, 0.25],
            y_range=[0, 1.1, 0.25],
            x_length=5,
            y_length=5,
            axis_config={"color": GREY, "include_tip": False},
            x_axis_config={"numbers_to_include": [0, 0.25, 0.5, 0.75, 1]},
            y_axis_config={"numbers_to_include": [0, 0.25, 0.5, 0.75, 1]},
        )
        axes.shift(DOWN * 0.3)

        x_label = axes.get_x_axis_label("x", direction=DOWN)
        y_label = axes.get_y_axis_label("y", direction=LEFT)

        # Unit square fill
        square_fill = axes.get_area(
            axes.plot(lambda x: 1.0, x_range=[0, 1], color=BLUE),
            x_range=[0, 1],
            color=BLUE_E,
            opacity=0.25,
        )

        # Unit square border
        corners = [
            axes.c2p(0, 0), axes.c2p(1, 0),
            axes.c2p(1, 1), axes.c2p(0, 1),
        ]
        square_border = Polygon(*corners, color=BLUE, stroke_width=2.5)

        # Omega label inside the square
        omega_label = MathTex(r"\Omega", font_size=52, color=BLUE_B)
        omega_label.move_to(axes.c2p(0.15, 0.88))

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(FadeIn(square_fill), Create(square_border), Write(omega_label))
        self.wait(1)

        # --- Animate dart points one by one ---
        xs = np.random.uniform(0.05, 0.95, 40)
        ys = np.random.uniform(0.05, 0.95, 40)

        dots = VGroup()
        for x, y in zip(xs, ys):
            dot = Dot(axes.c2p(x, y), radius=0.04, color=DOT_COLOR, fill_opacity=0.8)
            dots.add(dot)

        # Show dots in quick succession
        self.play(
            LaggedStart(*[FadeIn(d, scale=1.5) for d in dots],
                        lag_ratio=0.08, run_time=4.5),
        )
        self.wait(0.5)

        # --- Highlight one specific point ---
        hx, hy = 0.63, 0.41
        h_point = axes.c2p(hx, hy)

        h_dot = Dot(h_point, radius=0.07, color=HIGHLIGHT_COLOR, fill_opacity=1)
        h_dot.set_stroke(WHITE, width=1.5)

        # Crosshair lines
        v_line = DashedLine(
            axes.c2p(hx, 0), axes.c2p(hx, hy),
            color=HIGHLIGHT_COLOR, stroke_width=1.5, dash_length=0.07,
        )
        h_line = DashedLine(
            axes.c2p(0, hy), axes.c2p(hx, hy),
            color=HIGHLIGHT_COLOR, stroke_width=1.5, dash_length=0.07,
        )

        # Label for the highlighted point
        point_label = MathTex(
            r"(x, y) \text{ — one outcome}", font_size=22, color=HIGHLIGHT_COLOR
        )
        point_label.next_to(h_point, UR, buff=0.15)

        self.play(
            Create(v_line), Create(h_line),
            GrowFromCenter(h_dot),
        )
        self.play(Write(point_label))
        self.wait(1.5)

        # --- Key insight text ---
        insight = Text(
            "Uncountably many outcomes — cannot list them",
            font_size=24, color=WHITE,
        )
        insight.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(insight, shift=UP * 0.2))
        self.wait(2)

        # --- Math connection ---
        formula = MathTex(
            r"\Omega = \{(x, y) \mid 0 \le x \le 1,\ 0 \le y \le 1\}",
            font_size=22, color=GREY_A,
        )
        formula.next_to(insight, UP, buff=0.2)
        self.play(Write(formula))
        self.wait(2)

        # --- Summary ---
        self.play(FadeOut(VGroup(
            axes, x_label, y_label, square_fill, square_border,
            omega_label, dots, h_dot, v_line, h_line, point_label,
            insight, formula,
        )))
        summary = Text(
            "A continuous sample space has uncountably many outcomes.",
            font_size=28, color=WHITE,
        )
        self.play(Write(summary))
        self.wait(3)
        self.play(FadeOut(summary))
