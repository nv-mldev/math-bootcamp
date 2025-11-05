"""
Visualizations for probability axiom consequences:
1. Upper Bound: P(A) ≤ 1
2. Probability of Empty Set: P(∅) = 0
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Wedge, Circle
import numpy as np

# ============================================================================
# Visualization 1: Upper Bound P(A) ≤ 1
# ============================================================================

fig1, axes1 = plt.subplots(1, 3, figsize=(16, 5))
fig1.suptitle(
    r"Proof: For any event $A$, $P(A) \leq 1$", fontsize=16, fontweight="bold", y=1.02
)

# Define colors
color_A = "#FF6B6B"
color_Ac = "#4ECDC4"
color_omega = "#F0F0F0"

# Subplot 1: Show A and A^c partition Ω
ax1 = axes1[0]
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.set_aspect("equal")
ax1.axis("off")
ax1.set_title(
    r"Step 1: $A \cup A^c = \Omega$ (Partition)", fontsize=13, fontweight="bold", pad=10
)

# Draw sample space Ω as a rectangle
rect_omega = FancyBboxPatch(
    (1.5, 1.5),
    7,
    6,
    boxstyle="round,pad=0.15",
    edgecolor="black",
    facecolor=color_omega,
    linewidth=3,
    alpha=0.3,
)
ax1.add_patch(rect_omega)

# Draw A (left half)
rect_A = patches.Rectangle(
    (1.5, 1.5), 3.5, 6, facecolor=color_A, edgecolor="darkred", linewidth=2.5, alpha=0.6
)
ax1.add_patch(rect_A)

# Draw A^c (right half)
rect_Ac = patches.Rectangle(
    (5, 1.5), 3.5, 6, facecolor=color_Ac, edgecolor="teal", linewidth=2.5, alpha=0.6
)
ax1.add_patch(rect_Ac)

# Labels
ax1.text(
    3.25,
    4.5,
    r"$A$",
    fontsize=20,
    ha="center",
    va="center",
    fontweight="bold",
    color="darkred",
)
ax1.text(
    6.75,
    4.5,
    r"$A^c$",
    fontsize=20,
    ha="center",
    va="center",
    fontweight="bold",
    color="teal",
)
ax1.text(
    8.5,
    7.8,
    r"$\Omega$",
    fontsize=18,
    ha="center",
    va="center",
    fontweight="bold",
    color="black",
)

# Add note about disjoint
ax1.text(
    5,
    0.8,
    "Disjoint partition",
    fontsize=11,
    ha="center",
    style="italic",
    color="darkblue",
)

# Subplot 2: Apply probability axioms
ax2 = axes1[1]
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.set_aspect("equal")
ax2.axis("off")
ax2.set_title(r"Step 2: Apply Axioms", fontsize=13, fontweight="bold", pad=10)

# Show the equations
equations = [
    r"$P(A \cup A^c) = P(\Omega) = 1$",
    r"",
    r"By additivity axiom:",
    r"$P(A) + P(A^c) = 1$",
    r"",
    r"Rearranging:",
    r"$P(A) = 1 - P(A^c)$",
]

y_start = 8.5
for i, eq in enumerate(equations):
    if eq:
        fontsize = 14 if "$" in eq else 12
        weight = "bold" if "$" in eq else "normal"
        color_text = "darkblue" if i == 3 else "black"

        bbox_props = None
        if i == 3:
            bbox_props = dict(
                boxstyle="round,pad=0.4",
                facecolor="lightyellow",
                alpha=0.7,
                edgecolor="darkblue",
                linewidth=1.5,
            )

        ax2.text(
            5,
            y_start - i * 1.1,
            eq,
            fontsize=fontsize,
            ha="center",
            va="center",
            fontweight=weight,
            color=color_text,
            bbox=bbox_props,
        )

# Subplot 3: Conclude the inequality
ax3 = axes1[2]
ax3.set_xlim(0, 10)
ax3.set_ylim(0, 10)
ax3.set_aspect("equal")
ax3.axis("off")
ax3.set_title(r"Step 3: Apply Non-negativity", fontsize=13, fontweight="bold", pad=10)

# Show the final reasoning
final_eqs = [
    r"Since $P(A^c) \geq 0$",
    r"(non-negativity axiom)",
    r"",
    r"We have:",
    r"$1 - P(A^c) \leq 1$",
    r"",
    r"Therefore:",
    r"$P(A) \leq 1$",
]

y_start = 8.5
for i, eq in enumerate(final_eqs):
    if eq:
        fontsize = 14 if "$" in eq else 12
        weight = "bold" if i == 0 or i == 7 else "normal"
        color_text = "darkgreen" if i == 7 else "black"

        bbox_props = None
        if i == 7:
            bbox_props = dict(
                boxstyle="round,pad=0.5",
                facecolor="lightgreen",
                alpha=0.5,
                edgecolor="darkgreen",
                linewidth=2,
            )

        ax3.text(
            5,
            y_start - i * 0.95,
            eq,
            fontsize=fontsize,
            ha="center",
            va="center",
            fontweight=weight,
            color=color_text,
            bbox=bbox_props,
        )

plt.tight_layout()

# Save figure 1
output_path1 = (
    "/home/nithin/work/math-bootcamp/book/figures/probability_upper_bound.png"
)
plt.savefig(output_path1, dpi=300, bbox_inches="tight", facecolor="white")
print(f"Figure 1 saved to: {output_path1}")

# ============================================================================
# Visualization 2: Probability of Empty Set P(∅) = 0
# ============================================================================

fig2, axes2 = plt.subplots(1, 3, figsize=(16, 5))
fig2.suptitle(r"Proof: $P(\emptyset) = 0$", fontsize=16, fontweight="bold", y=1.02)

# Subplot 1: Show Ω and its complement (empty set)
ax1 = axes2[0]
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.set_aspect("equal")
ax1.axis("off")
ax1.set_title(
    r"Step 1: $\Omega^c = \emptyset$ (Definition)",
    fontsize=13,
    fontweight="bold",
    pad=10,
)

# Draw sample space Ω
circle_omega = Circle(
    (5, 5), 2.5, facecolor="lightblue", edgecolor="darkblue", linewidth=3, alpha=0.6
)
ax1.add_patch(circle_omega)
ax1.text(
    5,
    5,
    r"$\Omega$",
    fontsize=24,
    ha="center",
    va="center",
    fontweight="bold",
    color="darkblue",
)

# Show the universe boundary
rect_universe = patches.Rectangle(
    (1, 1),
    8,
    8,
    facecolor="none",
    edgecolor="black",
    linewidth=2,
    linestyle="--",
    alpha=0.3,
)
ax1.add_patch(rect_universe)

# Label the empty region outside
ax1.text(
    8.2,
    8.2,
    r"$\Omega^c = \emptyset$",
    fontsize=14,
    ha="center",
    va="center",
    fontweight="bold",
    color="gray",
    bbox=dict(
        boxstyle="round,pad=0.3", facecolor="white", edgecolor="gray", linewidth=1.5
    ),
)

# Add annotation
ax1.annotate(
    "",
    xy=(7.5, 7.5),
    xytext=(6.5, 6.5),
    arrowprops=dict(arrowstyle="->", lw=2, color="gray"),
)
ax1.text(
    5,
    0.5,
    "Nothing exists outside the sample space",
    fontsize=11,
    ha="center",
    style="italic",
    color="gray",
)

# Subplot 2: Apply probability axioms
ax2 = axes2[1]
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.set_aspect("equal")
ax2.axis("off")
ax2.set_title(
    r"Step 2: Express using Complement", fontsize=13, fontweight="bold", pad=10
)

# Show the equations
equations2 = [
    r"By normalization axiom:",
    r"$P(\Omega) = 1$",
    r"",
    r"By definition of complement:",
    r"$P(\Omega) + P(\Omega^c) = 1$",
    r"",
    r"Substituting $P(\Omega) = 1$:",
    r"$1 + P(\Omega^c) = 1$",
]

y_start = 8.5
for i, eq in enumerate(equations2):
    if eq:
        fontsize = 13 if "$" in eq else 11
        weight = "bold" if i == 1 or i == 4 else "normal"

        bbox_props = None
        if i == 4:
            bbox_props = dict(
                boxstyle="round,pad=0.3",
                facecolor="lightyellow",
                alpha=0.6,
                edgecolor="orange",
                linewidth=1.5,
            )

        ax2.text(
            5,
            y_start - i * 1.0,
            eq,
            fontsize=fontsize,
            ha="center",
            va="center",
            fontweight=weight,
            bbox=bbox_props,
        )

# Subplot 3: Final conclusion
ax3 = axes2[2]
ax3.set_xlim(0, 10)
ax3.set_ylim(0, 10)
ax3.set_aspect("equal")
ax3.axis("off")
ax3.set_title(
    r"Step 3: Solve for $P(\emptyset)$", fontsize=13, fontweight="bold", pad=10
)

# Show the final steps
final_eqs2 = [
    r"From: $1 + P(\Omega^c) = 1$",
    r"",
    r"Solving:",
    r"$P(\Omega^c) = 0$",
    r"",
    r"Since $\Omega^c = \emptyset$:",
    r"",
    r"$P(\emptyset) = 0$",
]

y_start = 8
for i, eq in enumerate(final_eqs2):
    if eq:
        fontsize = 15 if i == 7 else 13
        weight = "bold" if i == 7 or i == 3 else "normal"
        color_text = "darkgreen" if i == 7 else "black"

        bbox_props = None
        if i == 7:
            bbox_props = dict(
                boxstyle="round,pad=0.6",
                facecolor="lightgreen",
                alpha=0.6,
                edgecolor="darkgreen",
                linewidth=2.5,
            )

        ax3.text(
            5,
            y_start - i * 0.95,
            eq,
            fontsize=fontsize,
            ha="center",
            va="center",
            fontweight=weight,
            color=color_text,
            bbox=bbox_props,
        )

# Visual representation - empty set symbol
ax3.text(
    5,
    2,
    r"$\emptyset$",
    fontsize=80,
    ha="center",
    va="center",
    color="lightgray",
    alpha=0.3,
    fontweight="bold",
)
ax3.text(
    5,
    1,
    "Empty set has zero probability",
    fontsize=11,
    ha="center",
    style="italic",
    color="gray",
)

plt.tight_layout()

# Save figure 2
output_path2 = "/home/nithin/work/math-bootcamp/book/figures/probability_empty_set.png"
plt.savefig(output_path2, dpi=300, bbox_inches="tight", facecolor="white")
print(f"Figure 2 saved to: {output_path2}")

plt.show()
