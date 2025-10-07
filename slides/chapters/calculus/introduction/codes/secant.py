import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML


# Define the function
def f(x):
    return 0.5 * x**2 + 0.1 * x**3


# Fixed point P
x0 = 1.0
y0 = f(x0)

# Create figure for visualization
fig, ax = plt.subplots(figsize=(12, 8))


# Static visualization showing multiple secant lines
def create_static_secant_plot():
    ax.clear()

    # Plot the function
    x_vals = np.linspace(-0.5, 3, 400)
    y_vals = f(x_vals)
    label_str = "$f(x) = 0.5x^2 + 0.1x^3$"
    ax.plot(x_vals, y_vals, "b-", linewidth=3, label=label_str)

    # Fixed point P
    ax.plot(x0, y0, "ro", markersize=10, label=f"Point P({x0}, {y0:.2f})")

    # Different positions for point Q
    x1_values = [2.5, 2.0, 1.7, 1.4, 1.2, 1.1]
    colors = ["red", "orange", "yellow", "green", "cyan", "purple"]

    for i, x1 in enumerate(x1_values):
        y1 = f(x1)

        # Plot point Q
        ax.plot(x1, y1, "o", color=colors[i], markersize=8)

        # Calculate and plot secant line
        slope = (y1 - y0) / (x1 - x0)
        x_line = np.linspace(x0 - 0.3, x1 + 0.3, 100)
        y_line = y0 + slope * (x_line - x0)
        ax.plot(
            x_line,
            y_line,
            "--",
            color=colors[i],
            alpha=0.8,
            linewidth=2,
            label=f"Q at x={x1:.1f}, slope={slope:.2f}",
        )

    # Calculate true tangent line (derivative at x0)
    # f'(x) = x + 0.3x^2, so f'(1) = 1 + 0.3 = 1.3
    true_slope = x0 + 0.3 * x0**2
    x_tangent = np.linspace(x0 - 0.5, x0 + 1.5, 100)
    y_tangent = y0 + true_slope * (x_tangent - x0)
    ax.plot(
        x_tangent,
        y_tangent,
        "k-",
        linewidth=4,
        alpha=0.9,
        label=f"True tangent, slope={true_slope:.3f}",
    )

    ax.set_xlim(-0.2, 3)
    # Extended y-axis to show all points (y at x=2.5 is 4.69)
    ax.set_ylim(-0.5, 5.0)
    ax.set_xlabel("x", fontsize=14)
    ax.set_ylabel("f(x)", fontsize=14)
    ax.set_title("Secant Lines Approaching Tangent Line", fontsize=16)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper left", fontsize=10)


# Create the plot
create_static_secant_plot()

plt.tight_layout()

# Create figures directory if it doesn't exist
os.makedirs("figures", exist_ok=True)

plt.savefig("figures/secant_to_tangent_demo.png", dpi=150, bbox_inches="tight")
plt.show()

print("Key Observations:")
print("1. As Q approaches P, secant lines get closer to the tangent line")
print("2. The slopes of secant lines converge to the derivative value")
print("3. The tangent line represents the instantaneous rate of change at P")
