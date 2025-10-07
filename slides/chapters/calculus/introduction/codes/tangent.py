import numpy as np
import matplotlib.pyplot as plt


# Problem: Find the slope of y = x² at point P(2, 4) using first principle
def f(x):
    return x**2


# Point of interest
x0 = 2.0
y0 = f(x0)  # y0 = 4

print(f"Finding the slope of y = x² at point P({x0}, {y0}) using first principle")
print("=" * 60)

# Create figure with subplots to show secant lines approaching tangent
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle(
    f"First Principle: Slope of y = x² at P({x0}, {y0}) as h → 0",
    fontsize=16,
    fontweight="bold",
)

# Define h values (approaching 0)
h_values = [1.0, 0.5, 0.1, 0.01]
colors = ["red", "orange", "green", "purple"]
titles = [f"h = {h}" for h in h_values]

# Create x values for smooth curve
x = np.linspace(-0.5, 4.5, 400)
y = f(x)

axes = [ax1, ax2, ax3, ax4]

print("Secant line slopes:")
for i, (ax, h, color, title) in enumerate(zip(axes, h_values, colors, titles)):
    # Plot the parabola
    ax.plot(x, y, "b-", linewidth=2, label="y = x²", alpha=0.7)

    # Points for secant line
    x1 = x0
    x2 = x0 + h
    y1 = f(x1)
    y2 = f(x2)

    # Calculate secant slope using first principle formula
    secant_slope = (f(x0 + h) - f(x0)) / h

    # Plot the two points
    ax.plot(x1, y1, "ko", markersize=10, label=f"P({x1}, {y1})")
    ax.plot(x2, y2, "o", color=color, markersize=8, label=f"Q({x2:.2f}, {y2:.2f})")

    # Draw secant line
    x_secant = np.linspace(max(0, x1 - 1), min(5, x2 + 1), 100)
    y_secant = y1 + secant_slope * (x_secant - x1)
    ax.plot(
        x_secant,
        y_secant,
        "--",
        color=color,
        linewidth=2,
        alpha=0.8,
        label=f"Secant slope = {secant_slope:.4f}",
    )

    # Highlight the interval Δx = h
    ax.axvspan(x1, x2, alpha=0.2, color=color, label=f"Δx = h = {h}")

    # Add slope annotation
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    ax.annotate(
        f"Slope = {secant_slope:.4f}",
        xy=(mid_x, mid_y),
        xytext=(mid_x + 0.5, mid_y + 2),
        arrowprops=dict(arrowstyle="->", color=color, alpha=0.7),
        fontsize=10,
        color=color,
        fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
    )

    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.5, 16)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(title, fontweight="bold")
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=8, loc="upper left")

    print(
        f"h = {h:6.3f}: slope = (f({x0}+{h}) - f({x0}))/{h} = ({f(x0+h):.3f} - {f(x0):.3f})/{h} = {secant_slope:.6f}"
    )

plt.tight_layout()
plt.show()

# Show numerical convergence to the exact derivative
print("\nDetailed convergence as h approaches 0:")
print("h" + " " * 12 + "Secant Slope" + " " * 8 + "Error from 4")
print("-" * 40)

exact_slope = 4.0  # The derivative of x² at x=2 is 2x = 2(2) = 4

for h in [1.0, 0.1, 0.01, 0.001, 0.0001, 0.00001]:
    slope = (f(x0 + h) - f(x0)) / h
    error = abs(slope - exact_slope)
    print(f"{h:8.5f}     {slope:12.8f}     {error:10.8f}")

print(f"\nExact derivative at x = {x0}: f'({x0}) = 2x = 2({x0}) = {exact_slope}")

# Create a separate plot showing the tangent line
plt.figure(figsize=(10, 8))
x_plot = np.linspace(0, 4, 400)
y_plot = f(x_plot)

# Plot the parabola
plt.plot(x_plot, y_plot, "b-", linewidth=3, label="y = x²")

# Plot the point P(2, 4)
plt.plot(x0, y0, "ro", markersize=12, label=f"P({x0}, {y0})")

# Plot the tangent line: y - 4 = 4(x - 2) => y = 4x - 4
x_tangent = np.linspace(0.5, 3.5, 100)
y_tangent = exact_slope * (x_tangent - x0) + y0  # y - y0 = m(x - x0)
plt.plot(
    x_tangent,
    y_tangent,
    "r-",
    linewidth=3,
    label=f"Tangent: y = {exact_slope}x - {exact_slope * x0 - y0}",
)

# Add annotations
plt.annotate(
    f"P({x0}, {y0})",
    xy=(x0, y0),
    xytext=(x0 + 0.3, y0 + 1),
    arrowprops=dict(arrowstyle="->", color="red"),
    fontsize=12,
    fontweight="bold",
)

plt.annotate(
    f"Slope = {exact_slope}",
    xy=(2.5, exact_slope * (2.5 - x0) + y0),
    xytext=(3, 8),
    arrowprops=dict(arrowstyle="->", color="red"),
    fontsize=12,
    fontweight="bold",
    bbox=dict(boxstyle="round,pad=0.5", facecolor="yellow", alpha=0.8),
)

plt.xlim(0, 4)
plt.ylim(0, 16)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.title(f"Tangent Line to y = x² at P({x0}, {y0})", fontsize=14, fontweight="bold")
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()

# Final answer
print("\n" + "=" * 60)
print("SOLUTION:")
print("=" * 60)
print(f"The slope of y = x² at point P({x0}, {y0}) is: {exact_slope}")
print(f"The equation of the tangent line is: y - {y0} = {exact_slope}(x - {x0})")
print(f"Simplified: y = {exact_slope}x - {exact_slope * x0 - y0}")
print("=" * 60)
