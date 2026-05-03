from manim import *
import numpy as np


class CoinTree(Scene):
    """Probability tree for three coin flips, growing branch by branch."""

    def construct(self):
        # --- Title ---
        title = Text("Sequential Experiments: Tree Diagrams", font_size=40)
        subtitle = Text("Three coin flips — each path is one outcome", font_size=24, color=GREY)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(title), FadeIn(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

        # --- Node positions ---
        nodes = {
            "root": np.array([0, 2.5, 0]),
            "H":    np.array([-3, 1, 0]),
            "T":    np.array([3, 1, 0]),
            "HH":   np.array([-4.5, -0.5, 0]),
            "HT":   np.array([-1.5, -0.5, 0]),
            "TH":   np.array([1.5, -0.5, 0]),
            "TT":   np.array([4.5, -0.5, 0]),
            "HHH":  np.array([-5.5, -2.5, 0]),
            "HHT":  np.array([-3.5, -2.5, 0]),
            "HTH":  np.array([-2.0, -2.5, 0]),
            "HTT":  np.array([-0.5, -2.5, 0]),
            "THH":  np.array([0.5, -2.5, 0]),
            "THT":  np.array([2.0, -2.5, 0]),
            "TTH":  np.array([3.5, -2.5, 0]),
            "TTT":  np.array([5.5, -2.5, 0]),
        }

        leaf_heads = {
            "HHH": 3, "HHT": 2, "HTH": 2, "HTT": 1,
            "THH": 2, "THT": 1, "TTH": 1, "TTT": 0,
        }
        head_colors = {0: RED, 1: ORANGE, 2: GREEN, 3: BLUE}

        levels = [
            [("root","H","H"), ("root","T","T")],
            [("H","HH","H"), ("H","HT","T"), ("T","TH","H"), ("T","TT","T")],
            [("HH","HHH","H"), ("HH","HHT","T"), ("HT","HTH","H"), ("HT","HTT","T"),
             ("TH","THH","H"), ("TH","THT","T"), ("TT","TTH","H"), ("TT","TTT","T")],
        ]

        # Root
        root_dot = Dot(nodes["root"], color=WHITE, radius=0.12)
        root_label = Text("start", font_size=18, color=GREY)
        root_label.next_to(nodes["root"], UP, buff=0.1)
        self.play(GrowFromCenter(root_dot), Write(root_label))
        self.wait(0.3)

        # Stage labels
        stage_labels = VGroup(
            Text("Flip 1", font_size=18, color=GREY).move_to(LEFT * 6.2 + UP * 1),
            Text("Flip 2", font_size=18, color=GREY).move_to(LEFT * 6.2 + DOWN * 0.5),
            Text("Flip 3", font_size=18, color=GREY).move_to(LEFT * 6.2 + DOWN * 2.5),
        )
        self.play(FadeIn(stage_labels))

        # Build tree level by level — track all mobjects for later fadeout
        all_tree_mobs = VGroup(root_dot, root_label, stage_labels)
        leaf_dots = {}

        for level_edges in levels:
            anims = []
            for (parent, child, flip) in level_edges:
                edge = Line(nodes[parent], nodes[child],
                            color=GREY_B, stroke_width=1.5)
                flip_color = BLUE if flip == "H" else RED
                is_leaf = len(child) == 3
                dot = Dot(nodes[child],
                          color=head_colors[leaf_heads[child]] if is_leaf else WHITE,
                          radius=0.10 if is_leaf else 0.09)
                flip_label = Text(flip, font_size=16, color=flip_color)
                mid = (nodes[parent] + nodes[child]) / 2
                offset = LEFT * 0.18 if flip == "H" else RIGHT * 0.18
                flip_label.move_to(mid + offset)
                all_tree_mobs.add(edge, dot, flip_label)

                if is_leaf:
                    leaf_dots[child] = dot
                    prob_label = MathTex(r"\tfrac{1}{8}", font_size=14, color=GREY)
                    prob_label.next_to(nodes[child], DOWN, buff=0.08)
                    all_tree_mobs.add(prob_label)
                    anims.append(AnimationGroup(
                        Create(edge), GrowFromCenter(dot),
                        Write(flip_label), FadeIn(prob_label),
                    ))
                else:
                    node_label = Text(child, font_size=16, color=WHITE)
                    node_label.next_to(nodes[child],
                                       LEFT if child[0] == "H" else RIGHT, buff=0.08)
                    all_tree_mobs.add(node_label)
                    anims.append(AnimationGroup(
                        Create(edge), GrowFromCenter(dot),
                        Write(flip_label), Write(node_label),
                    ))

            self.play(LaggedStart(*anims, lag_ratio=0.15, run_time=2.5))
            self.wait(0.5)

        # --- Highlight event A: exactly 2 heads (3 leaves) ---
        two_heads = ["HHT", "HTH", "THH"]
        rings_a = VGroup(*[
            Circle(radius=0.18, color=YELLOW, stroke_width=3).move_to(nodes[n])
            for n in two_heads
        ])
        label_a = Text("Event A: exactly 2 heads   |A| = 3   P(A) = 3/8",
                       font_size=22, color=YELLOW)
        label_a.to_edge(DOWN, buff=0.5)
        self.play(Create(rings_a), Write(label_a))
        self.wait(2)

        # --- Transition to event B: at least 1 head (7 leaves) ---
        one_or_more = ["HHH","HHT","HTH","HTT","THH","THT","TTH"]
        rings_b = VGroup(*[
            Circle(radius=0.18, color=GREEN, stroke_width=3).move_to(nodes[n])
            for n in one_or_more
        ])
        label_b = Text("Event B: at least 1 head   |B| = 7   P(B) = 7/8",
                       font_size=22, color=GREEN)
        label_b.to_edge(DOWN, buff=0.5)
        self.play(FadeOut(rings_a), FadeOut(label_a))
        self.play(Create(rings_b), Write(label_b))
        self.wait(2)

        # --- Summary ---
        self.play(FadeOut(all_tree_mobs), FadeOut(rings_b), FadeOut(label_b))
        summary = Text(
            "A tree lists every sequential outcome exactly once.\nEvents are subsets of leaves — count them, divide by 8.",
            font_size=26, color=WHITE, line_spacing=1.5,
        )
        self.play(Write(summary))
        self.wait(3)
        self.play(FadeOut(summary))
