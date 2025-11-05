import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

fig, ax = plt.subplots(figsize=(12, 8))

# Create Venn diagram circles
circle_A = plt.Circle((0.35, 0.5), 0.25, color="blue", alpha=0.3, label="A")
circle_B = plt.Circle((0.65, 0.5), 0.25, color="red", alpha=0.3, label="B")

ax.add_patch(circle_A)
ax.add_patch(circle_B)

# Add labels
ax.text(0.25, 0.5, "A", fontsize=20, weight="bold", ha="center", va="center")
ax.text(0.75, 0.5, "B", fontsize=20, weight="bold", ha="center", va="center")
ax.text(
    0.5,
    0.5,
    r"$A \cap B$",
    fontsize=16,
    ha="center",
    va="center",
    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
)

# Rectangle for sample space
rect = FancyBboxPatch(
    (0.05, 0.15),
    0.9,
    0.7,
    boxstyle="round,pad=0.02",
    edgecolor="black",
    facecolor="lightgray",
    alpha=0.2,
    linewidth=2,
)
ax.add_patch(rect)
ax.text(0.1, 0.8, "S (Sample Space)", fontsize=14, style="italic")

# Add the identity formula
formula_text = r"$P(A \cup B) = P(A) + P(B) - P(A \cap B)$"
ax.text(
    0.5,
    0.05,
    formula_text,
    fontsize=20,
    ha="center",
    weight="bold",
    color="darkblue",
    bbox=dict(
        boxstyle="round,pad=0.5",
        facecolor="yellow",
        alpha=0.7,
        edgecolor="black",
        linewidth=2,
    ),
)

# Add explanation boxes on the right
explanation_y = 0.75
box_width = 0.35
box_x = 1.1

# Explanation 1
ax.text(
    box_x,
    explanation_y,
    "Why subtract P(A ∩ B)?",
    fontsize=14,
    weight="bold",
    ha="left",
)
ax.text(
    box_x, explanation_y - 0.08, "The intersection is counted", fontsize=11, ha="left"
)
ax.text(
    box_x, explanation_y - 0.13, "twice when we add P(A) + P(B)", fontsize=11, ha="left"
)

# Explanation 2
explanation_y2 = 0.5
ax.text(box_x, explanation_y2, "Visual proof:", fontsize=14, weight="bold", ha="left")
ax.text(
    box_x,
    explanation_y2 - 0.08,
    "1. P(A) includes the overlap",
    fontsize=11,
    ha="left",
    color="blue",
)
ax.text(
    box_x,
    explanation_y2 - 0.13,
    "2. P(B) includes the overlap",
    fontsize=11,
    ha="left",
    color="red",
)
ax.text(
    box_x,
    explanation_y2 - 0.18,
    "3. Subtract once to correct",
    fontsize=11,
    ha="left",
    color="purple",
)

ax.set_xlim(0, 1.6)
ax.set_ylim(0, 1)
ax.axis("off")
ax.set_aspect("equal")

plt.title(
    "Probability Union Identity Visualization", fontsize=18, weight="bold", pad=20
)
plt.tight_layout()

# Save the figure
import os

output_path = os.path.join(
    os.path.dirname(__file__), "../book/figures/probability_union_identity.png"
)
output_path = os.path.abspath(output_path)
plt.savefig(
    output_path, dpi=300, bbox_inches="tight", facecolor="white", edgecolor="none"
)
print(f"Image saved to: {output_path}")

plt.show()
