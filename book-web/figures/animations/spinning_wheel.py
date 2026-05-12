from manim import *
import numpy as np

WHEEL_RADIUS = 2.5
HIGHLIGHT = RED
ARC_COLOR = BLUE
POINTER_COLOR = RED


def angle_for_value(v: float) -> float:
    """Map value in [0,1] to angle in radians (0 at top, clockwise)."""
    return PI / 2 - 2 * PI * v


class SpinningWheelScene(Scene):
    """Spinning wheel shows why P(X = x) = 0 but P(interval) = length."""

    def construct(self):
        # ── Title card ──────────────────────────────────────────────
        title = Text("Continuous Sample Space", font_size=44)
        subtitle = Text("The Spinning Wheel", font_size=28, color=GREY)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(title), FadeIn(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

        # ── Build the wheel ─────────────────────────────────────────
        wheel = Circle(radius=WHEEL_RADIUS, color=WHITE, stroke_width=3)
        center_dot = Dot(ORIGIN, color=WHITE, radius=0.06)

        # Tick marks and labels at 0, 0.25, 0.5, 0.75, 1.0
        tick_values = [0.0, 0.25, 0.5, 0.75]          # 1.0 == 0.0
        tick_group = VGroup()
        label_group = VGroup()

        for v in tick_values:
            angle = angle_for_value(v)
            outer = WHEEL_RADIUS * np.array([np.cos(angle), np.sin(angle), 0])
            inner = (WHEEL_RADIUS - 0.18) * np.array([np.cos(angle), np.sin(angle), 0])
            tick = Line(inner, outer, color=GREY, stroke_width=2)
            tick_group.add(tick)

            label_pos = (WHEEL_RADIUS + 0.35) * np.array([np.cos(angle), np.sin(angle), 0])
            lbl_str = "0 / 1" if v == 0.0 else f"{v}"
            lbl = Text(lbl_str, font_size=22, color=GREY)
            lbl.move_to(label_pos)
            label_group.add(lbl)

        self.play(Create(wheel), FadeIn(center_dot), run_time=1)
        self.play(Create(tick_group), FadeIn(label_group), run_time=1)
        self.wait(0.5)

        # ── Pointer ─────────────────────────────────────────────────
        start_angle = angle_for_value(0.0)
        pointer_end = (WHEEL_RADIUS - 0.3) * np.array(
            [np.cos(start_angle), np.sin(start_angle), 0]
        )
        pointer = Arrow(
            ORIGIN, pointer_end,
            buff=0,
            color=POINTER_COLOR,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15,
        )
        self.play(GrowArrow(pointer), run_time=0.5)
        self.wait(0.5)

        # ── Spin animation ──────────────────────────────────────────
        # Land at value 0.3  →  total rotation = many full turns + offset
        land_value = 0.3
        land_angle = angle_for_value(land_value)
        # Spin 4 full turns clockwise then land
        total_rotation = -4 * 2 * PI - (start_angle - land_angle)

        self.play(
            Rotate(pointer, angle=total_rotation, about_point=ORIGIN,
                   rate_func=lambda t: t ** 0.4,   # fast then slow
                   run_time=3),
        )
        self.wait(0.5)

        # ── Mark the landed point ───────────────────────────────────
        land_pos = WHEEL_RADIUS * np.array(
            [np.cos(land_angle), np.sin(land_angle), 0]
        )
        land_dot = Dot(land_pos, color=POINTER_COLOR, radius=0.1)
        self.play(FadeIn(land_dot, scale=1.5), run_time=0.4)

        # Label: P(X = 0.3) = 0  — placed outside the wheel near the dot
        p_zero_label = MathTex(r"P(X = 0.3) = 0", font_size=28, color=POINTER_COLOR)
        p_zero_label.next_to(land_dot, RIGHT + UP, buff=0.2)
        self.play(Write(p_zero_label), run_time=0.8)
        self.wait(1.5)

        # ── Insight: why zero? ───────────────────────────────────────
        insight = Text(
            "Any single value has probability 0\n— there are infinitely many points.",
            font_size=22, color=YELLOW,
        )
        insight.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(insight), run_time=0.6)
        self.wait(2)
        self.play(FadeOut(insight), FadeOut(p_zero_label), FadeOut(land_dot))

        # ── Highlight arc [0.2, 0.5] ────────────────────────────────
        arc_start_angle = angle_for_value(0.2)
        arc_end_angle   = angle_for_value(0.5)
        # Arc sweeps clockwise from 0.2 to 0.5
        arc = Arc(
            radius=WHEEL_RADIUS,
            start_angle=arc_end_angle,
            angle=arc_start_angle - arc_end_angle,   # positive = CCW in Manim
            color=ARC_COLOR,
            stroke_width=8,
        )
        self.play(Create(arc), run_time=1)

        # Tick endpoints of the arc
        for v, direction in [(0.2, LEFT), (0.5, LEFT + DOWN)]:
            a = angle_for_value(v)
            pos = WHEEL_RADIUS * np.array([np.cos(a), np.sin(a), 0])
            d = Dot(pos, color=ARC_COLOR, radius=0.08)
            lbl = MathTex(str(v), font_size=22, color=ARC_COLOR)
            lbl.next_to(d, direction, buff=0.15)
            self.play(FadeIn(d), Write(lbl), run_time=0.3)

        self.wait(0.5)

        # Formula next to the arc
        formula = MathTex(
            r"P(0.2 \le X \le 0.5) = 0.5 - 0.2 = 0.3",
            font_size=26, color=ARC_COLOR,
        )
        formula.to_edge(DOWN, buff=0.5)
        self.play(Write(formula), run_time=1)
        self.wait(1)

        sub = Text("probability = length of interval", font_size=22, color=GREY)
        sub.next_to(formula, UP, buff=0.2)
        self.play(FadeIn(sub))
        self.wait(2)

        # ── Summary card ─────────────────────────────────────────────
        self.play(*[FadeOut(m) for m in self.mobjects])
        summary = Text(
            "On a continuous space, probability = length (or area).\nSingle points always have probability zero.",
            font_size=26, color=WHITE,
        )
        self.play(Write(summary))
        self.wait(3)
        self.play(FadeOut(summary))
