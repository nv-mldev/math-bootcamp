from manim import *
import numpy as np


class DiceSampleSpace(Scene):
    """The 6×6 grid of outcomes for rolling two dice, built cell by cell."""

    def construct(self):
        # --- Title ---
        title = Text("Sample Space: Two Dice", font_size=44)
        subtitle = Text("36 equally likely outcomes", font_size=26, color=GREY)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(title), FadeIn(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

        # --- Build the 6×6 grid ---
        cell_size = 0.8
        dot_colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]

        # Axis labels
        col_labels = VGroup()
        row_labels = VGroup()
        for i in range(1, 7):
            col_label = MathTex(str(i), font_size=22, color=GREY)
            col_label.move_to(RIGHT * (i - 3.5) * cell_size + UP * 2.8)
            col_labels.add(col_label)

            row_label = MathTex(str(i), font_size=22, color=GREY)
            row_label.move_to(LEFT * 3.2 + UP * (3.5 - i) * cell_size)
            row_labels.add(row_label)

        die1_label = Text("Die 1", font_size=20, color=GREY)
        die1_label.move_to(LEFT * 3.2 + UP * 3.1)
        die2_label = Text("Die 2 →", font_size=20, color=GREY)
        die2_label.move_to(UP * 3.15)

        self.play(Write(col_labels), Write(row_labels),
                  Write(die1_label), Write(die2_label))
        self.wait(0.3)

        # Build cells row by row
        cells = VGroup()
        dots = []
        for row in range(6):
            d1 = row + 1
            row_cells = VGroup()
            for col in range(6):
                d2 = col + 1
                cx = (col - 2.5) * cell_size
                cy = (2.5 - row) * cell_size

                square = Square(side_length=cell_size * 0.88,
                                color=WHITE, stroke_width=0.8, fill_opacity=0)
                square.move_to([cx, cy, 0])

                label = MathTex(f"({d1},{d2})", font_size=16, color=WHITE)
                label.move_to([cx, cy, 0])

                row_cells.add(VGroup(square, label))

            cells.add(row_cells)
            self.play(
                LaggedStart(*[FadeIn(c, scale=0.8) for c in row_cells],
                            lag_ratio=0.1, run_time=0.6),
            )

        self.wait(0.5)

        # --- Highlight: sum = 7 ---
        sum7_cells = []
        sum7_squares = VGroup()
        combos = [(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)]
        for (d1, d2) in combos:
            row, col = d1 - 1, d2 - 1
            cx = (col - 2.5) * cell_size
            cy = (2.5 - row) * cell_size
            highlight = Square(side_length=cell_size * 0.88,
                               color=YELLOW, stroke_width=3,
                               fill_color=YELLOW, fill_opacity=0.3)
            highlight.move_to([cx, cy, 0])
            sum7_squares.add(highlight)

        event_label = Text("Event A: sum = 7  (6 outcomes)", font_size=24, color=YELLOW)
        event_label.to_edge(DOWN, buff=0.5)

        self.play(FadeIn(sum7_squares), Write(event_label))
        self.wait(1.5)

        # Show probability
        prob_label = MathTex(
            r"P(A) = \frac{|A|}{|\Omega|} = \frac{6}{36} = \frac{1}{6}",
            font_size=30, color=YELLOW,
        )
        prob_label.next_to(event_label, UP, buff=0.2)
        self.play(Write(prob_label))
        self.wait(2)

        # --- Summary ---
        self.play(FadeOut(VGroup(
            cells, col_labels, row_labels, die1_label, die2_label,
            sum7_squares, event_label, prob_label,
        )))
        summary = Text(
            "A sample space lists every possible outcome — no more, no less.",
            font_size=26, color=WHITE,
        )
        self.play(Write(summary))
        self.wait(3)
        self.play(FadeOut(summary))
