#!/usr/bin/env python3

from manim import *


class RealNumberLine(Scene):
    def construct(self):
        # Title
        title = Text("The Real Number Line", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create a number line
        number_line = NumberLine(
            x_range=[-5, 5, 1],
            length=10,
            include_numbers=True,
            include_tip=True,
        )

        # Add labels for different types of numbers
        labels = VGroup()

        # Label for integers
        int_label = Text("Integers (ℤ)", font_size=24, color=BLUE)
        int_label.next_to(number_line, DOWN, buff=1.5).shift(LEFT * 3)
        int_arrow = Arrow(int_label.get_top(), number_line.n2p(2), buff=0.2, color=BLUE)

        # Label for rational numbers
        rat_label = Text("Rational Numbers (ℚ)", font_size=24, color=GREEN)
        rat_label.next_to(number_line, DOWN, buff=1.5)
        rat_arrow = Arrow(
            rat_label.get_top(), number_line.n2p(1.5), buff=0.2, color=GREEN
        )

        # Label for irrational numbers
        irr_label = Text("Irrational Numbers", font_size=24, color=YELLOW)
        irr_label.next_to(number_line, DOWN, buff=1.5).shift(RIGHT * 3)
        irr_arrow = Arrow(
            irr_label.get_top(), number_line.n2p(3.14), buff=0.2, color=YELLOW
        )

        labels.add(int_label, int_arrow, rat_label, rat_arrow, irr_label, irr_arrow)

        # Show the number line
        self.play(Create(number_line))
        self.wait(1)

        # Show the labels
        self.play(
            FadeIn(int_label),
            Create(int_arrow),
        )
        self.wait(0.5)

        self.play(
            FadeIn(rat_label),
            Create(rat_arrow),
        )
        self.wait(0.5)

        self.play(
            FadeIn(irr_label),
            Create(irr_arrow),
        )
        self.wait(2)

        # Clean up for the next part
        self.play(
            FadeOut(title),
            FadeOut(labels),
            FadeOut(number_line),
        )
        self.wait(1)


class ModularArithmetic(Scene):
    def construct(self):
        # Title
        title = Text("Modular Arithmetic", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create a circular number line for modulo 12 (like a clock)
        radius = 2.5
        circle = Circle(radius=radius, color=WHITE)

        # Create hour marks and numbers for the clock (mod 12)
        hours = VGroup()
        hour_labels = VGroup()

        for i in range(12):
            angle = i * (TAU / 12)

            # Hour mark
            hour_mark = Line(
                radius * 0.9 * np.array([np.cos(angle), np.sin(angle), 0]),
                radius * np.array([np.cos(angle), np.sin(angle), 0]),
                stroke_width=3,
            )

            # Hour number
            if i == 0:
                hour_num = 12
            else:
                hour_num = i

            hour_label = Text(str(hour_num), font_size=24)
            hour_label.move_to(
                radius * 1.2 * np.array([np.cos(angle), np.sin(angle), 0])
            )

            hours.add(hour_mark)
            hour_labels.add(hour_label)

        # Add explanation text
        mod_12_text = Text(
            "In mod 12: 3 ≡ 15 ≡ 27 ≡ 39 (mod 12)", font_size=30, color=YELLOW
        ).next_to(circle, DOWN, buff=1)

        mod_example = MathTex(
            r"15 \div 12 = 1 \text{ remainder } 3", font_size=30
        ).next_to(mod_12_text, DOWN)

        # Create animations
        self.play(Create(circle))
        self.play(Create(hours), Write(hour_labels))
        self.wait(1)

        # Show modular equivalence with arrows
        arrows = VGroup()
        for num in [3, 15, 27, 39]:
            # Convert to equivalent position on mod 12 clock
            equiv = num % 12
            if equiv == 0:
                equiv = 12

            angle = ((equiv - 3) * (TAU / 12)) % TAU
            arrow = Arrow(
                ORIGIN,
                0.9 * radius * np.array([np.cos(angle), np.sin(angle), 0]),
                buff=0,
                color=YELLOW,
                stroke_width=4,
            )
            arrows.add(arrow)

        # Show one arrow at a time
        for i, arrow in enumerate(arrows):
            self.play(GrowArrow(arrow))
            if i > 0:
                self.play(FadeOut(arrows[i - 1]))
            self.wait(0.5)

        self.play(FadeOut(arrows[-1]))
        self.wait(1)

        # Show text explanation
        self.play(Write(mod_12_text))
        self.wait(1)
        self.play(Write(mod_example))
        self.wait(2)

        # Clean up
        self.play(
            FadeOut(VGroup(circle, hours, hour_labels, mod_12_text, mod_example)),
            FadeOut(title),
        )
        self.wait(1)


class ModularIntervals(Scene):
    def construct(self):
        # Title
        title = Text("Intervals in Modular Arithmetic", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create a number line for mod 7
        mod = 7
        number_line = NumberLine(
            x_range=[0, 14, 1],
            length=10,
            include_numbers=True,
        )

        # Label for modulus
        mod_label = Text(f"mod {mod}", font_size=36)
        mod_label.next_to(number_line, DOWN, buff=0.5)

        self.play(Create(number_line), Write(mod_label))
        self.wait(1)

        # Highlight the modular equivalence classes
        classes = VGroup()

        for i in range(mod):
            dots = VGroup()
            for j in range(3):  # Show a few repetitions
                pos = i + j * mod
                if 0 <= pos <= 14:  # Stay within the number line range
                    dot = Dot(number_line.n2p(pos), color=BLUE)
                    dots.add(dot)

            classes.add(dots)

        # Show each equivalence class one at a time
        for i, equiv_class in enumerate(classes):
            self.play(FadeIn(equiv_class, shift=UP * 0.5), run_time=0.7)

            # Add a label for this equivalence class
            class_label = MathTex(
                f"[{i}]_{{7}} = ", f"\\{{ {i}, {i+7}, {i+14}, ... \\}}", font_size=30
            )
            class_label.set_color_by_tex(f"\\{{ {i}", BLUE)
            class_label.next_to(number_line, UP, buff=0.5 + i * 0.6)

            self.play(Write(class_label))
            self.wait(0.5)

        self.wait(2)

        # Clean up
        self.play(FadeOut(VGroup(number_line, mod_label, *classes)), FadeOut(title))
        self.wait(1)


# Main scene that combines all the concepts
class RealLineAndModularArithmetic(Scene):
    def construct(self):
        # Display title
        main_title = Text("Real Number Line & Modular Arithmetic", font_size=48)
        self.play(Write(main_title))
        self.wait(1)
        self.play(FadeOut(main_title))

        # Create and play each scene
        real_line = RealNumberLine()
        real_line.construct()

        mod_arithmetic = ModularArithmetic()
        mod_arithmetic.construct()

        mod_intervals = ModularIntervals()
        mod_intervals.construct()

        # Final message
        final_message = Text(
            "Mathematics: Where Continuous Meets Discrete", font_size=36
        )
        self.play(Write(final_message))
        self.wait(2)
        self.play(FadeOut(final_message))
