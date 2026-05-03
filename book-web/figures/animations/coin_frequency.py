from manim import *
import numpy as np

rng = np.random.default_rng(seed=0)
N = 300
flips = rng.integers(0, 2, size=N)
running_freq = np.cumsum(flips) / np.arange(1, N + 1)


class CoinFrequency(Scene):
    """Running frequency of heads converging to 0.5 as flips accumulate."""

    def construct(self):
        # --- Title ---
        title = Text("The Frequentist View", font_size=44)
        subtitle = Text("Long-run frequency → probability", font_size=26, color=GREY)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(title), FadeIn(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

        # --- Axes ---
        axes = Axes(
            x_range=[0, N, 50],
            y_range=[0, 1, 0.25],
            x_length=10,
            y_length=5,
            axis_config={"color": GREY, "include_tip": False},
            x_axis_config={"numbers_to_include": [50, 100, 150, 200, 250, 300]},
            y_axis_config={"numbers_to_include": [0, 0.25, 0.5, 0.75, 1.0]},
        )
        axes.shift(DOWN * 0.3)
        x_label = axes.get_x_axis_label("\\text{Number of flips}", direction=DOWN)
        y_label = axes.get_y_axis_label("\\text{Fraction heads}", direction=LEFT)

        # True probability line
        true_p_line = DashedLine(
            axes.c2p(0, 0.5), axes.c2p(N, 0.5),
            color=RED, stroke_width=2, dash_length=0.15,
        )
        true_p_label = MathTex(r"p = 0.5", font_size=24, color=RED)
        true_p_label.next_to(axes.c2p(N, 0.5), RIGHT, buff=0.1)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(true_p_line), Write(true_p_label))
        self.wait(0.5)

        # --- Animate the running frequency line growing ---
        # Build points for the frequency curve
        points = [axes.c2p(i + 1, running_freq[i]) for i in range(N)]

        # Draw in 3 phases: noisy start (1-30), settling (30-100), converged (100-300)
        phase1 = VMobject(color=BLUE, stroke_width=2.5)
        phase1.set_points_as_corners(points[:30])

        phase2 = VMobject(color=BLUE, stroke_width=2.5)
        phase2.set_points_as_corners(points[29:100])

        phase3 = VMobject(color=BLUE, stroke_width=2.5)
        phase3.set_points_as_corners(points[99:])

        # Annotation for chaotic start
        chaos_label = Text("Noisy — only a few flips", font_size=22, color=YELLOW)
        chaos_label.next_to(axes.c2p(15, running_freq[15]), UP, buff=0.2)

        self.play(Create(phase1), run_time=1.5)
        self.play(FadeIn(chaos_label))
        self.wait(0.5)

        settle_label = Text("Settling toward 0.5", font_size=22, color=GREEN)
        settle_label.next_to(axes.c2p(65, running_freq[65]), UP, buff=0.2)

        self.play(FadeOut(chaos_label), Create(phase2), run_time=2)
        self.play(FadeIn(settle_label))
        self.wait(0.5)

        converge_label = Text("Converged — zigzag shrinks", font_size=22, color=BLUE)
        converge_label.next_to(axes.c2p(200, running_freq[199]), UP, buff=0.2)

        self.play(FadeOut(settle_label), Create(phase3), run_time=2.5)
        self.play(FadeIn(converge_label))
        self.wait(1.5)

        # --- Key insight ---
        insight = Text(
            '"Probability" is the limit this frequency converges to.',
            font_size=24, color=WHITE,
        )
        insight.to_edge(DOWN, buff=0.4)
        self.play(FadeOut(converge_label), FadeIn(insight, shift=UP * 0.2))
        self.wait(2)

        # --- Cleanup + summary ---
        self.play(FadeOut(VGroup(
            axes, x_label, y_label, true_p_line, true_p_label,
            phase1, phase2, phase3, insight,
        )))
        summary = Text(
            "Frequency is not probability — but it converges to it.",
            font_size=28, color=WHITE,
        )
        self.play(Write(summary))
        self.wait(3)
        self.play(FadeOut(summary))
