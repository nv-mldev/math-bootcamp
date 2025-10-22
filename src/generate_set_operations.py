#!/usr/bin/env python3
"""
Generate set operation diagrams using matplotlib-venn
This script creates visualizations for various set operations and saves them to the figures directory.
"""

import os
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3
import numpy as np
from matplotlib.patches import Circle, Rectangle
from matplotlib.collections import PatchCollection

# Create figures directory if it doesn't exist
os.makedirs("../book/figures/set_operations", exist_ok=True)

# Set the default figure size
plt.rcParams["figure.figsize"] = (8, 6)
plt.rcParams["font.size"] = 14


def save_figure(filename):
    """Save the figure to the specified filename in the figures directory."""
    filepath = f"../book/figures/set_operations/{filename}"
    plt.savefig(filepath, bbox_inches="tight", dpi=300)
    print(f"Saved {filepath}")
    plt.close()


# 1. Intersection (A ∩ B)
def create_intersection():
    plt.figure()

    # Create Venn diagram with custom colors
    v = venn2(subsets=(10, 10, 5), set_labels=("A", "B"))

    # Set colors - only highlight intersection
    v.get_patch_by_id("10").set_color("none")  # A only - transparent
    v.get_patch_by_id("10").set_edgecolor("black")
    v.get_patch_by_id("01").set_color("none")  # B only - transparent
    v.get_patch_by_id("01").set_edgecolor("black")
    v.get_patch_by_id("11").set_color("#9370DB")  # Intersection - purple

    plt.title(r"Intersection: $A \cap B$")
    save_figure("intersection.png")


# 2. Union (A ∪ B)
def create_union():
    plt.figure()

    # Create Venn diagram
    v = venn2(subsets=(10, 10, 5), set_labels=("A", "B"))

    # Set all regions to light blue
    v.get_patch_by_id("10").set_color("#B3E0FF")  # A only
    v.get_patch_by_id("01").set_color("#B3E0FF")  # B only
    v.get_patch_by_id("11").set_color("#B3E0FF")  # Intersection

    plt.title(r"Union: $A \cup B$")
    save_figure("union.png")


# 3. Set Difference (A ∩ B^c)
def create_difference():
    plt.figure()

    # Create Venn diagram
    v = venn2(subsets=(10, 10, 5), set_labels=("A", "B"))

    # Set colors - only highlight A\B
    v.get_patch_by_id("10").set_color("#FF7F7F")  # A only - red
    v.get_patch_by_id("01").set_color("none")  # B only - transparent
    v.get_patch_by_id("01").set_edgecolor("black")
    v.get_patch_by_id("11").set_color("none")  # Intersection - transparent
    v.get_patch_by_id("11").set_edgecolor("black")

    plt.title(r"Set Difference: $A \cap B^c$ or $A \setminus B$")
    save_figure("difference.png")


# 4. Subset (B ⊂ A)
def create_subset():
    fig, ax = plt.subplots()

    # Create circles
    circle_a = plt.Circle((0.5, 0.5), 0.4, fill=False, edgecolor="black", linewidth=2)
    circle_b = plt.Circle(
        (0.5, 0.5), 0.2, fill=True, color="#90EE90", alpha=0.7
    )  # Light green

    # Add circles to plot
    ax.add_patch(circle_a)
    ax.add_patch(circle_b)

    # Add labels
    plt.text(0.5, 0.5, "B", ha="center", va="center")
    plt.text(0.5, 0.8, "A", ha="center", va="center")

    # Set plot properties
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")

    plt.title(r"Subset: $B \subset A$")
    save_figure("subset.png")


# 5. Complement (A^c)
def create_complement():
    fig, ax = plt.subplots()

    # Create universe rectangle
    universe = Rectangle(
        (0.1, 0.1), 0.8, 0.8, fill=True, color="#FFCC99", alpha=0.5
    )  # Light orange

    # Create circle A
    circle_a = plt.Circle(
        (0.5, 0.5), 0.25, fill=True, color="white", edgecolor="black", linewidth=2
    )

    # Add shapes to plot
    ax.add_patch(universe)
    ax.add_patch(circle_a)

    # Add labels
    plt.text(0.5, 0.5, "A", ha="center", va="center")
    plt.text(0.2, 0.85, "Ω", ha="center", va="center", fontsize=16)

    # Shade the complement area
    plt.text(0.8, 0.7, "$A^c$", ha="center", va="center", fontsize=14)

    # Set plot properties
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")

    plt.title(r"Complement: $A^c$")
    save_figure("complement.png")


# 6. Disjoint Sets
def create_disjoint():
    plt.figure()

    # Create Venn diagram
    v = venn2(subsets=(10, 10, 0), set_labels=("A", "B"))

    # Set colors
    v.get_patch_by_id("10").set_color("#FF9999")  # A - light red
    v.get_patch_by_id("01").set_color("#99CCFF")  # B - light blue

    # Since the circles don't overlap, there's no '11' patch

    plt.title("Disjoint Sets: $A \cap B = \emptyset$")
    save_figure("disjoint.png")


# 7. Partition
def create_partition():
    fig, ax = plt.subplots()

    # Create universe as a square
    universe_size = 0.8
    x_start = 0.1
    y_start = 0.1

    # Draw universe outline
    universe = Rectangle(
        (x_start, y_start),
        universe_size,
        universe_size,
        fill=False,
        edgecolor="black",
        linestyle="-",
        linewidth=2,
    )
    ax.add_patch(universe)

    # Create a partition with four clearly separated rectangular regions
    # This approach completely eliminates any potential overlap or diagonal lines

    # Create the regions using simple rectangles for clean separation

    # Partition A - Top left rectangle
    partition_a = Rectangle(
        (x_start, y_start + universe_size / 2),  # Bottom left corner of rectangle
        universe_size / 2,  # Width
        universe_size / 2,  # Height
        fill=True,
        facecolor="#FF9999",  # Light red
        alpha=0.8,
        edgecolor="black",
        linewidth=1,
    )
    ax.add_patch(partition_a)

    # Partition B - Bottom right rectangle
    partition_b = Rectangle(
        (x_start + universe_size / 2, y_start),  # Bottom left corner of rectangle
        universe_size / 2,  # Width
        universe_size / 2,  # Height
        fill=True,
        facecolor="#99CCFF",  # Light blue
        alpha=0.8,
        edgecolor="black",
        linewidth=1,
    )
    ax.add_patch(partition_b)

    # Partition C - Bottom left rectangle
    partition_c = Rectangle(
        (x_start, y_start),  # Bottom left corner of rectangle
        universe_size / 2,  # Width
        universe_size / 2,  # Height
        fill=True,
        facecolor="#90EE90",  # Light green
        alpha=0.8,
        edgecolor="black",
        linewidth=1,
    )
    ax.add_patch(partition_c)

    # Partition D - Top right rectangle
    partition_d = Rectangle(
        (
            x_start + universe_size / 2,
            y_start + universe_size / 2,
        ),  # Bottom left corner
        universe_size / 2,  # Width
        universe_size / 2,  # Height
        fill=True,
        facecolor="#FF69B4",  # Hot pink
        alpha=0.8,
        edgecolor="black",
        linewidth=1,
    )
    ax.add_patch(partition_d)  # Add labels
    plt.text(
        x_start + universe_size / 3,
        y_start + 0.7 * universe_size,
        "A",
        ha="center",
        va="center",
        fontsize=16,
    )
    plt.text(
        x_start + 0.75 * universe_size,
        y_start + 0.25 * universe_size,
        "B",
        ha="center",
        va="center",
        fontsize=16,
    )
    plt.text(
        x_start + 0.25 * universe_size,
        y_start + 0.25 * universe_size,
        "C",
        ha="center",
        va="center",
        fontsize=16,
    )
    plt.text(
        x_start + 0.75 * universe_size,
        y_start + 0.75 * universe_size,
        "D",
        ha="center",
        va="center",
        fontsize=16,
    )

    # Add universe label
    plt.text(
        x_start - 0.05,
        y_start + universe_size + 0.05,
        "Ω",
        ha="center",
        va="center",
        fontsize=16,
    )

    # Set plot properties
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")

    plt.title("Partition of Ω")
    save_figure("partition.png")


# 8. Symmetric Difference (A △ B)
def create_symmetric_difference():
    plt.figure()

    # Create Venn diagram
    v = venn2(subsets=(10, 10, 5), set_labels=("A", "B"))

    # Set colors
    v.get_patch_by_id("10").set_color("#FF9999")  # A only - light red
    v.get_patch_by_id("01").set_color("#99CCFF")  # B only - light blue
    v.get_patch_by_id("11").set_color("none")  # Intersection - transparent
    v.get_patch_by_id("11").set_edgecolor("black")

    plt.title(r"Symmetric Difference: $A \triangle B$")
    save_figure("symmetric_difference.png")


# Generate all diagrams
if __name__ == "__main__":
    create_intersection()
    create_union()
    create_difference()
    create_subset()
    create_complement()
    create_disjoint()
    create_partition()
    create_symmetric_difference()

    # Create a combined figure showing all operations
    fig, axs = plt.subplots(2, 4, figsize=(16, 8))

    # Flatten the array for easy iteration
    axs = axs.flatten()

    # List of operations and their file names
    operations = [
        ("Intersection: $A \\cap B$", "intersection.png"),
        ("Union: $A \\cup B$", "union.png"),
        ("Set Difference: $A \\setminus B$", "difference.png"),
        ("Subset: $B \\subset A$", "subset.png"),
        ("Complement: $A^c$", "complement.png"),
        ("Disjoint Sets", "disjoint.png"),
        ("Partition of $\\Omega$", "partition.png"),
        ("Symmetric Difference: $A \\triangle B$", "symmetric_difference.png"),
    ]

    # Add each operation to the subplot
    for i, (title, filename) in enumerate(operations):
        img = plt.imread(f"../book/figures/set_operations/{filename}")
        axs[i].imshow(img)
        axs[i].set_title(title, fontsize=12)
        axs[i].axis("off")

    plt.tight_layout()
    plt.savefig(
        "../book/figures/set_operations/all_operations.png",
        dpi=300,
        bbox_inches="tight",
    )
    print("Saved combined figure")
    plt.close()

    print("All set operation diagrams have been generated.")
