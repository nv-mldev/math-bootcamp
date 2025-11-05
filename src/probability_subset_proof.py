"""
Visualization of the proof that if A ⊂ B, then P(A) ≤ P(B)
Shows how B can be decomposed into A ∪ (B ∩ A^c)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Create figure with subplots
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle(
    r"Proof: If $A \subset B$, then $P(A) \leq P(B)$",
    fontsize=16,
    fontweight="bold",
    y=1.02,
)

# Define colors
color_A = "#FF6B6B"
color_B_minus_A = "#4ECDC4"
color_B = "#95E1D3"

# Subplot 1: Show A ⊂ B
ax1 = axes[0]
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.set_aspect("equal")
ax1.axis("off")
ax1.set_title(r"Step 1: Given $A \subset B$", fontsize=13, fontweight="bold", pad=10)

# Draw set B (outer rectangle)
rect_B = FancyBboxPatch(
    (2, 2),
    6,
    5,
    boxstyle="round,pad=0.1",
    edgecolor="darkblue",
    facecolor=color_B,
    linewidth=2.5,
    alpha=0.3,
)
ax1.add_patch(rect_B)

# Draw set A (inner rectangle)
rect_A = FancyBboxPatch(
    (3, 3),
    4,
    3,
    boxstyle="round,pad=0.05",
    edgecolor="darkred",
    facecolor=color_A,
    linewidth=2.5,
    alpha=0.5,
)
ax1.add_patch(rect_A)

# Labels
ax1.text(
    5,
    4.5,
    r"$A$",
    fontsize=18,
    ha="center",
    va="center",
    fontweight="bold",
    color="darkred",
)
ax1.text(
    7.2,
    6.5,
    r"$B$",
    fontsize=18,
    ha="center",
    va="center",
    fontweight="bold",
    color="darkblue",
)

# Subplot 2: Show decomposition B = A ∪ (B ∩ A^c)
ax2 = axes[1]
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.set_aspect("equal")
ax2.axis("off")
ax2.set_title(
    r"Step 2: Decompose $B = A \cup (B \cap A^c)$",
    fontsize=13,
    fontweight="bold",
    pad=10,
)

# Draw B ∩ A^c (the part of B outside A) with pattern
# We'll draw this as the full B first
rect_B2 = FancyBboxPatch(
    (2, 2),
    6,
    5,
    boxstyle="round,pad=0.1",
    edgecolor="darkblue",
    facecolor=color_B_minus_A,
    linewidth=2.5,
    alpha=0.4,
)
ax2.add_patch(rect_B2)

# Then draw A on top
rect_A2 = FancyBboxPatch(
    (3, 3),
    4,
    3,
    boxstyle="round,pad=0.05",
    edgecolor="darkred",
    facecolor=color_A,
    linewidth=2.5,
    alpha=0.6,
)
ax2.add_patch(rect_A2)

# Add hatching to show B ∩ A^c region
rect_hatch = FancyBboxPatch(
    (2, 2),
    6,
    5,
    boxstyle="round,pad=0.1",
    edgecolor="none",
    facecolor="none",
    linewidth=0,
    hatch="///",
    alpha=0.3,
)
ax2.add_patch(rect_hatch)

# Labels
ax2.text(
    5,
    4.5,
    r"$A$",
    fontsize=18,
    ha="center",
    va="center",
    fontweight="bold",
    color="darkred",
)
ax2.text(
    3,
    6,
    r"$B \cap A^c$",
    fontsize=14,
    ha="center",
    va="center",
    fontweight="bold",
    color="teal",
    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
)

# Add brace showing these are disjoint
ax2.annotate(
    "",
    xy=(2.5, 1.5),
    xytext=(7.5, 1.5),
    arrowprops=dict(arrowstyle="<->", lw=2, color="darkblue"),
)
ax2.text(
    5,
    1,
    r"$B$ (disjoint union)",
    fontsize=12,
    ha="center",
    fontweight="bold",
    color="darkblue",
)

# Subplot 3: Show the probability inequality
ax3 = axes[2]
ax3.set_xlim(0, 10)
ax3.set_ylim(0, 10)
ax3.set_aspect("equal")
ax3.axis("off")
ax3.set_title(r"Step 3: Apply Additivity Axiom", fontsize=13, fontweight="bold", pad=10)

# Show the equation breakdown
equations = [
    r"$P(B) = P(A) + P(B \cap A^c)$",
    r"",
    r"Since $P(B \cap A^c) \geq 0$:",
    r"",
    r"$P(B) \geq P(A)$",
]

y_start = 8
for i, eq in enumerate(equations):
    if eq:
        fontsize = 15 if "$P(B)" in eq else 13
        weight = "bold" if i == 0 or i == 4 else "normal"
        color = "darkblue" if i == 4 else "black"

        bbox_props = None
        if i == 4:
            bbox_props = dict(
                boxstyle="round,pad=0.5",
                facecolor="yellow",
                alpha=0.3,
                edgecolor="darkblue",
                linewidth=2,
            )

        ax3.text(
            5,
            y_start - i * 1.2,
            eq,
            fontsize=fontsize,
            ha="center",
            va="center",
            fontweight=weight,
            color=color,
            bbox=bbox_props,
        )

# Add visual representation with bars
bar_y = 2.5
bar_height = 0.8

# P(A) bar
rect_bar_A = patches.Rectangle(
    (1.5, bar_y),
    3,
    bar_height,
    facecolor=color_A,
    edgecolor="darkred",
    linewidth=2,
    alpha=0.7,
)
ax3.add_patch(rect_bar_A)
ax3.text(
    3,
    bar_y + bar_height / 2,
    r"$P(A)$",
    fontsize=12,
    ha="center",
    va="center",
    fontweight="bold",
)

# P(B ∩ A^c) bar
rect_bar_B_minus_A = patches.Rectangle(
    (4.5, bar_y),
    2,
    bar_height,
    facecolor=color_B_minus_A,
    edgecolor="teal",
    linewidth=2,
    alpha=0.7,
)
ax3.add_patch(rect_bar_B_minus_A)
ax3.text(
    5.5,
    bar_y + bar_height / 2,
    r"$P(B \cap A^c)$",
    fontsize=10,
    ha="center",
    va="center",
    fontweight="bold",
)

# Brace showing P(B)
ax3.plot([1.5, 6.5], [bar_y - 0.3, bar_y - 0.3], "k-", linewidth=2)
ax3.plot([1.5, 1.5], [bar_y - 0.3, bar_y - 0.5], "k-", linewidth=2)
ax3.plot([6.5, 6.5], [bar_y - 0.3, bar_y - 0.5], "k-", linewidth=2)
ax3.text(
    4,
    bar_y - 0.8,
    r"$P(B)$",
    fontsize=12,
    ha="center",
    fontweight="bold",
    color="darkblue",
)

# Add note about non-negativity
ax3.text(
    7.5,
    bar_y + bar_height / 2,
    r"$\geq 0$",
    fontsize=12,
    ha="center",
    va="center",
    color="green",
    fontweight="bold",
    bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen", alpha=0.5),
)

plt.tight_layout()

# Save the figure
output_path = (
    "/home/nithin/work/math-bootcamp/book/figures/probability_subset_proof.png"
)
plt.savefig(output_path, dpi=300, bbox_inches="tight", facecolor="white")
print(f"Figure saved to: {output_path}")

plt.show()
