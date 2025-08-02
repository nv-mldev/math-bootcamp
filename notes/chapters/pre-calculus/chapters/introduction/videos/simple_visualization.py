#!/usr/bin/env python3
"""
A simpler version of the real line and modular arithmetic visualizations
that can be run with just matplotlib without requiring manim.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrow, Circle


# Set the style
plt.style.use("dark_background")


def real_number_line():
    """Create a visualization of the real number line"""
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(-6, 6)
    ax.set_ylim(-3, 3)

    # Draw the number line
    ax.axhline(y=0, color="white", linestyle="-", linewidth=2)

    # Add arrow at the end
    ax.arrow(
        5.7,
        0,
        0.3,
        0,
        head_width=0.2,
        head_length=0.2,
        fc="white",
        ec="white",
        linewidth=2,
    )

    # Add tick marks and labels for integers
    ticks = range(-5, 6)
    ax.set_xticks(ticks)
    ax.set_xticklabels([str(t) for t in ticks], fontsize=12)

    # Add special point labels
    special_points = {
        "π": 3.14159,
        "√2": 1.414,
        "-√3": -1.732,
        "e": 2.718,
    }

    for label, value in special_points.items():
        ax.plot(value, 0, "o", markersize=8, color="yellow")
        ax.text(value, 0.3, label, fontsize=14, ha="center", color="yellow")

    # Add category labels
    ax.text(
        -4,
        -1,
        "Negative\nIntegers",
        fontsize=12,
        ha="center",
        va="center",
        color="lightblue",
    )
    ax.text(0, -1, "Zero", fontsize=12, ha="center", va="center", color="white")
    ax.text(
        3,
        -1,
        "Positive\nIntegers",
        fontsize=12,
        ha="center",
        va="center",
        color="lightblue",
    )

    # Add example irrational and rational points
    ax.text(
        1.5,
        1,
        "Rational numbers (can be written as fractions)",
        fontsize=12,
        ha="center",
        va="center",
        color="lightgreen",
    )
    ax.text(
        3,
        2,
        "Irrational numbers (cannot be written as fractions)",
        fontsize=12,
        ha="center",
        va="center",
        color="yellow",
    )

    # Add arrows to examples
    ax.arrow(
        1.5,
        0.7,
        0,
        -0.5,
        head_width=0.1,
        head_length=0.1,
        fc="lightgreen",
        ec="lightgreen",
        linewidth=1,
    )
    ax.arrow(
        3.14,
        1.7,
        0,
        -1.5,
        head_width=0.1,
        head_length=0.1,
        fc="yellow",
        ec="yellow",
        linewidth=1,
    )

    # Add title and axis labels
    ax.set_title("The Real Number Line (ℝ)", fontsize=18, pad=20)
    ax.text(6, 0, "x", fontsize=14, ha="left")

    # Remove y-axis ticks
    ax.set_yticks([])

    # Set background color
    ax.set_facecolor("black")
    fig.tight_layout()

    # Save the figure
    plt.savefig("real_number_line.png", dpi=150, bbox_inches="tight")
    plt.close()


def modular_arithmetic_clock():
    """Create a visualization of modular arithmetic using a clock face (mod 12)"""
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={"aspect": "equal"})
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)

    # Draw the clock face
    circle = Circle((0, 0), 4, fill=False, color="white", linewidth=2)
    ax.add_artist(circle)

    # Add hour marks and numbers
    for i in range(12):
        angle = i * (2 * np.pi / 12)
        x = 3.8 * np.cos(angle)
        y = 3.8 * np.sin(angle)

        # Hour mark
        hour_mark_inner_x = 3.5 * np.cos(angle)
        hour_mark_inner_y = 3.5 * np.sin(angle)
        ax.plot([hour_mark_inner_x, x], [hour_mark_inner_y, y], "white", linewidth=2)

        # Hour number
        num_x = 4.3 * np.cos(angle)
        num_y = 4.3 * np.sin(angle)
        hour_num = 12 if i == 0 else i
        ax.text(
            num_x,
            num_y,
            str(hour_num),
            fontsize=14,
            ha="center",
            va="center",
            color="white",
        )

    # Add examples of congruent numbers
    congruent_examples = [3, 15, 27]

    # Use different colors for different congruence classes
    colors = ["red", "yellow", "cyan", "magenta"]

    for i, num in enumerate(congruent_examples):
        # Calculate position on the clock (mod 12)
        equiv = num % 12
        if equiv == 0:
            equiv = 12

        angle = (equiv - 3) * (2 * np.pi / 12)

        # Draw arrow
        arrow = FancyArrow(
            0,
            0,
            2.5 * np.cos(angle),
            2.5 * np.sin(angle),
            width=0.1,
            length_includes_head=True,
            head_width=0.3,
            head_length=0.3,
            color=colors[i % len(colors)],
        )
        ax.add_patch(arrow)

        # Add text explanation
        ax.text(
            0,
            -3 - 0.5 * i,
            f"{num} ≡ {equiv} (mod 12)",
            fontsize=14,
            ha="center",
            va="center",
            color=colors[i % len(colors)],
        )

    # Add title
    ax.set_title("Modular Arithmetic (Mod 12)", fontsize=18, pad=20)

    # Remove axes
    ax.set_xticks([])
    ax.set_yticks([])

    # Set background color
    ax.set_facecolor("black")
    fig.tight_layout()

    # Save the figure
    plt.savefig("modular_arithmetic_clock.png", dpi=150, bbox_inches="tight")
    plt.close()


def modular_intervals():
    """Create a visualization of intervals in modular arithmetic"""
    fig, axes = plt.subplots(3, 1, figsize=(12, 10), height_ratios=[1, 1, 1.5])

    # Mod 7 number line
    mod = 7
    ax = axes[0]
    ax.set_xlim(-1, 15)
    ax.set_ylim(-2, 2)

    # Draw the number line
    ax.axhline(y=0, color="white", linestyle="-", linewidth=2)

    # Add tick marks and labels
    ticks = range(0, 15)
    ax.set_xticks(ticks)
    ax.set_xticklabels([str(t) for t in ticks], fontsize=12)

    # Highlight equivalent classes with colors
    colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

    for i in range(mod):
        # Draw dots for equivalent values
        for j in range(3):  # Show 3 repetitions
            pos = i + j * mod
            if pos < 15:
                ax.plot(pos, 0, "o", markersize=10, color=colors[i])

        # Add label for equivalence class
        ax.text(
            i + 0.5 * mod,
            1,
            f"[{i}]₇",
            fontsize=14,
            ha="center",
            va="center",
            color=colors[i],
        )

    ax.set_title("Equivalence Classes in Mod 7", fontsize=16)
    ax.set_yticks([])

    # Mod 7 clock
    ax = axes[1]
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect("equal")

    # Draw the clock face
    circle = Circle((0, 0), 3, fill=False, color="white", linewidth=2)
    ax.add_artist(circle)

    # Add hour marks and numbers
    for i in range(7):
        angle = i * (2 * np.pi / 7)
        x = 2.8 * np.cos(angle)
        y = 2.8 * np.sin(angle)

        # Hour mark
        hour_mark_inner_x = 2.5 * np.cos(angle)
        hour_mark_inner_y = 2.5 * np.sin(angle)
        ax.plot([hour_mark_inner_x, x], [hour_mark_inner_y, y], "white", linewidth=2)

        # Hour number
        num_x = 3.3 * np.cos(angle)
        num_y = 3.3 * np.sin(angle)
        ax.text(
            num_x, num_y, str(i), fontsize=14, ha="center", va="center", color=colors[i]
        )

    ax.set_title("Mod 7 Clock", fontsize=16)
    ax.set_xticks([])
    ax.set_yticks([])

    # Examples of calculations in mod 7
    ax = axes[2]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)

    # Add text with examples
    examples = [
        "3 + 5 = 8 ≡ 1 (mod 7)",
        "6 + 4 = 10 ≡ 3 (mod 7)",
        "2 × 4 = 8 ≡ 1 (mod 7)",
        "3 × 5 = 15 ≡ 1 (mod 7)",
        "6 × 6 = 36 ≡ 1 (mod 7)",
    ]

    for i, example in enumerate(examples):
        ax.text(1, 4 - 0.7 * i, example, fontsize=14, color="white")

    ax.set_title("Examples of Calculations in Mod 7", fontsize=16)
    ax.set_xticks([])
    ax.set_yticks([])

    # Set background color for all subplots
    for ax in axes:
        ax.set_facecolor("black")

    fig.tight_layout()

    # Save the figure
    plt.savefig("modular_intervals.png", dpi=150, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    print("Generating visualizations...")
    real_number_line()
    print("- Real number line visualization saved as 'real_number_line.png'")
    modular_arithmetic_clock()
    print(
        "- Modular arithmetic clock visualization saved as 'modular_arithmetic_clock.png'"
    )
    modular_intervals()
    print("- Modular intervals visualization saved as 'modular_intervals.png'")
    print("Done!")
