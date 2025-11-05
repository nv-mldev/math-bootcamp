import matplotlib.pyplot as plt
import numpy as np

# Pascal's Triangle rows
triangle = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]

fig, ax = plt.subplots(figsize=(10, 8))
ax.axis("off")

# Draw triangle
for row_idx, row in enumerate(triangle):
    for col_idx, val in enumerate(row):
        x = col_idx - row_idx / 2
        y = -row_idx
        ax.text(
            x,
            y,
            str(val),
            fontsize=18,
            ha="center",
            va="center",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="gray"),
        )

# Highlight Pascal's Identity for n=5, k=2
# 10 = 4 + 6
highlight = [(2, 5), (1, 4), (2, 4)]
colors = ["#ffeb3b", "#90caf9", "#90caf9"]
for (col, row), color in zip(highlight, colors):
    x = col - row / 2
    y = -row
    ax.text(
        x,
        y,
        str(triangle[row][col]),
        fontsize=18,
        ha="center",
        va="center",
        bbox=dict(boxstyle="round,pad=0.3", facecolor=color, edgecolor="black", lw=2),
    )


# Add arrows
def arrow(from_row, from_col, to_row, to_col):
    x1 = from_col - from_row / 2
    y1 = -from_row
    x2 = to_col - to_row / 2
    y2 = -to_row
    ax.annotate(
        "",
        xy=(x2, y2 + 0.3),
        xytext=(x1, y1 - 0.3),
        arrowprops=dict(arrowstyle="->", lw=2, color="red"),
    )


arrow(4, 1, 5, 2)
arrow(4, 2, 5, 2)

# Add identity label
ax.text(
    2 - 5 / 2,
    -5.7,
    r"$\binom{5}{2} = \binom{4}{1} + \binom{4}{2}$",
    fontsize=20,
    color="darkred",
    ha="center",
    weight="bold",
)
ax.text(2 - 5 / 2, -6.2, "10 = 4 + 6", fontsize=16, color="darkgreen", ha="center")

# Add title
ax.text(
    0, 0.5, "Pascal's Identity Visualization", fontsize=22, ha="center", weight="bold"
)

plt.tight_layout()

# Save the figure
plt.savefig("../book/figures/pascal_identity.png", dpi=300, bbox_inches="tight")
print("Image saved to: ../book/figures/pascal_identity.png")

# Display the plot
plt.show()
