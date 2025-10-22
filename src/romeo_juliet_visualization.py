#!/usr/bin/env python3
"""
Visualization of the Romeo and Juliet meeting probability problem.

This script generates a visualization showing:
1. The sample space (unit square)
2. The region where Romeo and Juliet meet (within 15 minutes)
3. The probability calculation using geometric areas
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def create_romeo_juliet_visualization():
    """Create the main visualization for the Romeo and Juliet problem."""

    # Create figure with single plot
    fig, ax1 = plt.subplots(1, 1, figsize=(8, 8))

    # Subplot 1: Geometric visualization
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.set_aspect('equal')
    ax1.set_xlabel("Romeo's delay (hours)", fontsize=12, fontweight='bold')
    ax1.set_ylabel("Juliet's delay (hours)", fontsize=12, fontweight='bold')
    ax1.set_title("Romeo and Juliet Meeting Problem\n(Geometric View)",
                  fontsize=14, fontweight='bold', pad=15)
    ax1.grid(True, alpha=0.3, linestyle='--')

    # Draw the unit square (sample space)
    square = patches.Rectangle((0, 0), 1, 1, linewidth=2,
                               edgecolor='black', facecolor='lightgray',
                               alpha=0.3, label='Sample Space')
    ax1.add_patch(square)

    # Define the meeting region: |x - y| <= 0.25
    # This creates a band between y = x - 0.25 and y = x + 0.25

    # Create vertices for the meeting region (hexagonal shape)
    meeting_x = [0, 0.25, 1, 1, 0.75, 0, 0]
    meeting_y = [0, 0, 0.75, 1, 1, 0.25, 0]

    # Fill the meeting region
    ax1.fill(meeting_x, meeting_y, color='lightgreen', alpha=0.6,
             label='They Meet (|x-y| ≤ 0.25)')

    # Draw boundary lines
    x_line = np.linspace(0, 1, 100)
    ax1.plot(x_line, x_line - 0.25, 'r--', linewidth=2,
             label='y = x - 0.25', alpha=0.8)
    ax1.plot(x_line, x_line + 0.25, 'b--', linewidth=2,
             label='y = x + 0.25', alpha=0.8)

    # Draw the diagonal y = x for reference
    ax1.plot([0, 1], [0, 1], 'k-', linewidth=1.5, alpha=0.5,
             label='y = x (same arrival)')

    # Add corner triangles annotation
    # Upper left triangle
    triangle1_x = [0, 0, 0.75, 0]
    triangle1_y = [0.25, 1, 1, 0.25]
    ax1.fill(triangle1_x, triangle1_y, color='red', alpha=0.2)
    ax1.text(0.15, 0.8, 'Miss\n(Juliet early)', fontsize=9,
             ha='center', va='center', style='italic')

    # Lower right triangle
    triangle2_x = [0.25, 1, 1, 0.25]
    triangle2_y = [0, 0, 0.75, 0]
    ax1.fill(triangle2_x, triangle2_y, color='red', alpha=0.2)
    ax1.text(0.8, 0.15, 'Miss\n(Romeo early)', fontsize=9,
             ha='center', va='center', style='italic')

    # Add sample points to show the concept
    np.random.seed(42)
    n_samples = 200
    romeo_delays = np.random.uniform(0, 1, n_samples)
    juliet_delays = np.random.uniform(0, 1, n_samples)

    # Determine which pairs meet
    meet = np.abs(romeo_delays - juliet_delays) <= 0.25

    # Plot sample points
    ax1.scatter(romeo_delays[meet], juliet_delays[meet], c='green',
               s=10, alpha=0.4, label=f'Meet ({np.sum(meet)} samples)')
    ax1.scatter(romeo_delays[~meet], juliet_delays[~meet], c='red',
               s=10, alpha=0.4, label=f'Miss ({np.sum(~meet)} samples)')

    ax1.legend(loc='upper right', fontsize=10)

    # Add simulation result as text on the main plot
    simulated_prob = np.sum(meet) / n_samples
    ax1.text(0.5, -0.08,
             f'Monte Carlo Simulation: {n_samples} samples | '
             f'Empirical: {simulated_prob:.3f} ({simulated_prob:.1%}) | '
             f'Theoretical: 7/16 = 0.4375 (43.75%)',
             fontsize=10, ha='center', transform=ax1.transAxes,
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

    plt.tight_layout()
    return fig


def create_interactive_visualization():
    """Create an interactive visualization showing different wait times."""

    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    wait_times = [0.1, 0.25, 0.5, 0.75]  # Different wait times in hours

    for idx, (ax, wait_time) in enumerate(zip(axes.flat, wait_times)):
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect('equal')
        ax.set_xlabel("Romeo's delay (hours)", fontsize=10)
        ax.set_ylabel("Juliet's delay (hours)", fontsize=10)

        # Calculate probability for this wait time
        area_miss = 2 * 0.5 * (1 - wait_time) ** 2
        area_meet = 1 - area_miss
        prob_meet = area_meet

        ax.set_title(f'Wait time: {wait_time*60:.0f} min | P(meet) = {prob_meet:.3f} = {prob_meet:.1%}',
                    fontsize=11, fontweight='bold')

        # Draw sample space
        square = patches.Rectangle((0, 0), 1, 1, linewidth=2,
                                   edgecolor='black', facecolor='lightgray', alpha=0.3)
        ax.add_patch(square)

        # Meeting region vertices
        if wait_time < 1:
            meeting_x = [0, wait_time, 1, 1, 1-wait_time, 0, 0]
            meeting_y = [0, 0, 1-wait_time, 1, 1, wait_time, 0]
        else:
            meeting_x = [0, 1, 1, 0, 0]
            meeting_y = [0, 0, 1, 1, 0]

        ax.fill(meeting_x, meeting_y, color='lightgreen', alpha=0.6)

        # Boundary lines
        x_line = np.linspace(0, 1, 100)
        ax.plot(x_line, x_line - wait_time, 'r--', linewidth=1.5, alpha=0.7)
        ax.plot(x_line, x_line + wait_time, 'b--', linewidth=1.5, alpha=0.7)
        ax.plot([0, 1], [0, 1], 'k-', linewidth=1, alpha=0.3)

        ax.grid(True, alpha=0.3, linestyle='--')

    plt.suptitle('Romeo and Juliet Problem: Effect of Wait Time on Meeting Probability',
                fontsize=14, fontweight='bold', y=0.995)
    plt.tight_layout()
    return fig


if __name__ == '__main__':
    # Generate the main visualization
    print("Generating Romeo and Juliet meeting probability visualization...")

    fig1 = create_romeo_juliet_visualization()
    fig1.savefig('../book/figures/romeo_juliet_probability.png',
                dpi=300, bbox_inches='tight')
    print("✓ Saved: ../book/figures/romeo_juliet_probability.png")

    fig2 = create_interactive_visualization()
    fig2.savefig('../book/figures/romeo_juliet_wait_times.png',
                dpi=300, bbox_inches='tight')
    print("✓ Saved: ../book/figures/romeo_juliet_wait_times.png")

    print("\nVisualizations created successfully!")
    print(f"Theoretical probability: 7/16 = {7/16:.4f} = {7/16:.2%}")
