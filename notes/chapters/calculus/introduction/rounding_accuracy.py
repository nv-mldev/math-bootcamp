import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Set up the figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Parameters
true_distance = 762  # km (true distance)
true_time = 15  # hours
speed_limit = 50  # km/h
rounding_error = 3  # km (potential error in either direction)

# Calculate true average speed
true_avg_speed = true_distance / true_time

# Plot 1: Effect of distance rounding on average speed
distances = np.linspace(
    true_distance - rounding_error, true_distance + rounding_error, 100
)
avg_speeds = distances / true_time

# Plot the data
ax1.plot(distances, avg_speeds, "b-", linewidth=2)
ax1.axhline(
    y=speed_limit, color="r", linestyle="--", label=f"Speed Limit ({speed_limit} km/h)"
)
ax1.axhline(
    y=true_avg_speed,
    color="g",
    linestyle="-",
    label=f"True Average Speed ({true_avg_speed:.1f} km/h)",
)
ax1.axvline(
    x=true_distance,
    color="g",
    linestyle="-",
    label=f"True Distance ({true_distance} km)",
)

# Highlight the rounding zones
ax1.axvspan(
    true_distance - 0.5,
    true_distance + 0.5,
    alpha=0.2,
    color="green",
    label="Rounded to True Distance",
)
ax1.axvspan(
    true_distance - rounding_error,
    true_distance - 0.5,
    alpha=0.2,
    color="orange",
    label=f"Potential Under-reporting",
)
ax1.axvspan(
    true_distance + 0.5,
    true_distance + rounding_error,
    alpha=0.2,
    color="orange",
    label=f"Potential Over-reporting",
)

# Set labels
ax1.set_xlabel("Measured Distance (km)", fontsize=12)
ax1.set_ylabel("Average Speed (km/h)", fontsize=12)
ax1.set_title("How Distance Measurement Affects Average Speed", fontsize=14)
ax1.grid(True, alpha=0.3)
ax1.legend(loc="upper left", fontsize=10)

# Plot 2: Bar chart showing rounding effects and speed limit violations
distances_rounded = [
    true_distance - 3,
    true_distance - 2,
    true_distance - 1,
    true_distance,
    true_distance + 1,
    true_distance + 2,
    true_distance + 3,
]
speeds_rounded = [d / true_time for d in distances_rounded]

# Create bars
bars = ax2.bar(
    distances_rounded,
    speeds_rounded,
    width=0.7,
    alpha=0.7,
    color=["red" if speed >= speed_limit else "green" for speed in speeds_rounded],
)

# Add speed limit line
ax2.axhline(
    y=speed_limit, color="r", linestyle="--", label=f"Speed Limit ({speed_limit} km/h)"
)

# Add values on bars
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax2.text(
        bar.get_x() + bar.get_width() / 2.0,
        height + 0.1,
        f"{speeds_rounded[i]:.1f}",
        ha="center",
        va="bottom",
        fontsize=9,
    )

    # Indicate whether it's over the speed limit
    if speeds_rounded[i] >= speed_limit:
        ax2.text(
            bar.get_x() + bar.get_width() / 2.0,
            height / 2,
            "OVER\nLIMIT",
            ha="center",
            va="center",
            fontsize=9,
            fontweight="bold",
            color="white",
        )

# Set labels
ax2.set_xlabel("Reported Distance (km)", fontsize=12)
ax2.set_ylabel("Average Speed (km/h)", fontsize=12)
ax2.set_title("Potential Speed Limit Violations Due to Rounding", fontsize=14)
ax2.grid(True, axis="y", alpha=0.3)
ax2.legend()

# Add text explanation in the figure
plt.figtext(
    0.5,
    0.01,
    "This visualization demonstrates how small changes in distance measurements (e.g., due to rounding)\n"
    "can affect average speed calculations, potentially pushing the computed speed above or below a critical threshold.",
    ha="center",
    fontsize=10,
    bbox={"facecolor": "lightgray", "alpha": 0.3, "pad": 5},
)

# Adjust layout
plt.tight_layout(rect=[0, 0.05, 1, 0.97])
plt.subplots_adjust(bottom=0.17)

# Add a title for the entire figure
fig.suptitle(
    "Rounding and Accuracy: Impact on Average Speed Calculations",
    fontsize=16,
    fontweight="bold",
)

# Create figures directory if it doesn't exist
import os

os.makedirs("figures", exist_ok=True)

# Save the figure
plt.savefig("figures/rounding_accuracy_demo.png", dpi=150, bbox_inches="tight")
plt.show()

print("\nKey Observations:")
print("1. Small measurement errors can push calculated speeds above/below thresholds")
print("2. For a journey of 762 km over 15 hours:")
print(f"   - True average speed: {true_avg_speed:.2f} km/h")
print(f"   - With -3 km error: {(true_distance-3)/true_time:.2f} km/h")
print(f"   - With +3 km error: {(true_distance+3)/true_time:.2f} km/h")
print("3. Distances between 759-762 km result in speeds below the 50 km/h limit")
print("4. Distances between 763-765 km result in speeds above the 50 km/h limit")
print(
    "\nConclusion: Precision in data collection is critical when the results are used"
)
print(
    "to make decisions near threshold values (like speed limits, legal boundaries, etc.)"
)
