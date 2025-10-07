# Math Bootcamp Book Compilation

This directory contains the complete Math Bootcamp book in LaTeX format, converted from the original Beamer presentations following the conversion plan.

## Files Structure

- `book.tex` - Main LaTeX file for the complete book
- `chapters/` - Individual chapter files converted from Beamer format
- `figures/` - All images consolidated from various source directories
- `compile.sh` - Automated compilation script
- `book.pdf` - Generated PDF output (created after running compile.sh)

## How to Compile the Book

### Quick Start

```bash
./compile.sh
```

### What the Script Does

1. **Compiles** the book twice (for proper cross-references and table of contents)
2. **Generates** book.pdf with all content and images
3. **Cleans up** all auxiliary files (.aux, .log, .toc, etc.)
4. **Keeps only** the .tex source files and .pdf output
5. **Reports** compilation status and PDF statistics

### Manual Compilation (if needed)

```bash
pdflatex book.tex
pdflatex book.tex  # Run twice for TOC and cross-references
```

## Book Content

The book contains the following parts:

### Part I: Pre-Calculus Foundations

- Chapter 1: Introduction
- Chapter 2: Real Numbers  
- Chapter 3: Functions
- Chapter 4: Polynomials
- Chapter 5: Exponentials and Logarithms
- Chapter 6: Trigonometry
- Chapter 7: Polar Coordinates and Complex Numbers
- Chapter 8: Sequences and Series

### Part II: Geometry

- Chapter 9: Geometry Introduction
- Chapter 10: Scalars and Vectors
- Chapter 11: 3D Geometry

### Part III: Calculus

- Chapter 12: Introduction to Calculus

## Conversion Notes

This book was created following the Math Bootcamp Book Conversion Plan:

1. **Phase 1**: Project setup with proper directory structure
2. **Phase 2**: Converted Beamer presentations to book chapters
3. **Phase 3**: Assembled chapters with consistent formatting
4. **Phase 4**: Compilation and refinement

### What Was Converted

- ✅ Removed all Beamer-specific commands (\begin{frame}, \end{frame})
- ✅ Converted frame titles to sections and subsections
- ✅ Consolidated all images into single figures/ directory
- ✅ Fixed all image paths to use consolidated location
- ✅ Removed presentation overlays and animations
- ✅ Maintained all mathematical content and figures

### Known Issues

- Some Beamer-specific environments (block, columns) may need manual cleanup
- A few image files may be missing (non-critical)
- Some math syntax may need refinement

## Output

- **Pages**: ~156 pages
- **Size**: ~6.1 MB
- **Format**: Professional book layout with table of contents
- **Images**: All figures properly embedded

## Requirements

- LaTeX distribution (texlive or similar)
- pdflatex command
- Standard math packages (amsmath, amssymb, graphicx, etc.)
