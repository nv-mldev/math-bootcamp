# Real Line and Modular Arithmetic Animations

This directory contains Manim animations that demonstrate:

1. The real number line
2. Modular arithmetic concepts
3. Intervals in modular arithmetic

## Prerequisites

Before running these animations, you need to install Manim. Here's how to set it up:

```bash
# Make sure you have Python 3.7 or higher installed
pip install manim

# You'll also need additional dependencies
# For MacOS:
brew install cairo ffmpeg

# For detailed installation instructions, visit:
# https://docs.manim.community/en/stable/installation.html
```

## Running the animations

To render a scene with low quality (for quick testing):

```bash
manim -pql real_line_and_modular.py RealNumberLine
```

To render with medium quality:

```bash
manim -pqm real_line_and_modular.py RealNumberLine
```

To render with high quality:

```bash
manim -pqh real_line_and_modular.py RealNumberLine
```

Replace `RealNumberLine` with any of these scene classes:

- `RealNumberLine`
- `ModularArithmetic`
- `ModularIntervals`
- `RealLineAndModularArithmetic` (the full animation)

## Output

The rendered videos will be saved in the `media` directory that Manim creates.
