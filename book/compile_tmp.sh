#!/bin/bash

# Math Bootcamp Book Compilation Script
# This script compiles the main.tex file and cleans up auxiliary files

echo "======================================"
echo "Math Bootcamp Book Compilation Script"
echo "======================================"

# Check if book.tex exists
if [ ! -f "book.tex" ]; then
    echo "Error: book.tex not found in current directory!"
    echo "Please run this script from the book directory."
    exit 1
fi

echo "Starting compilation..."

# Compile the book (run twice for proper cross-references and TOC)
echo "First pass compilation..."
pdflatex -interaction=nonstopmode book.tex > compile.log 2>&1

if [ $? -ne 0 ]; then
    echo "Warning: First pass had errors. Check compile.log for details."
fi

echo "Second pass compilation (for cross-references and TOC)..."
pdflatex -interaction=nonstopmode book.tex >> compile.log 2>&1

if [ $? -ne 0 ]; then
    echo "Warning: Second pass had errors. Check compile.log for details."
fi

# Check if PDF was generated
if [ -f "book.pdf" ]; then
    echo "✓ PDF generated successfully: book.pdf"
    
    # Get PDF info
    if command -v pdfinfo > /dev/null 2>&1; then
        pages=$(pdfinfo book.pdf 2>/dev/null | grep "Pages:" | awk '{print $2}')
        if [ ! -z "$pages" ]; then
            echo "✓ PDF contains $pages pages"
        fi
        
        size=$(ls -lh book.pdf | awk '{print $5}')
        echo "✓ PDF size: $size"
    fi
else
    echo "✗ Error: PDF was not generated!"
    echo "Check compile.log for error details."
    exit 1
fi

# Clean up auxiliary files (keep only .pdf and .tex files)
echo ""
echo "Cleaning up auxiliary files..."

# List of extensions to remove
aux_extensions=("aux" "log" "toc" "out" "nav" "snm" "fls" "fdb_latexmk" "synctex.gz")

removed_count=0

for ext in "${aux_extensions[@]}"; do
    for file in *.$ext chapters/*.$ext; do
        if [ -f "$file" ]; then
            rm "$file"
            echo "Removed: $file"
            ((removed_count++))
        fi
    done
done

# Remove compile log created by this script
if [ -f "compile.log" ]; then
    rm "compile.log"
    echo "Removed: compile.log"
    ((removed_count++))
fi

# Remove any backup files
for file in *~ chapters/*~; do
    if [ -f "$file" ]; then
        rm "$file"
        echo "Removed: $file"
        ((removed_count++))
    fi
done

echo ""
if [ $removed_count -gt 0 ]; then
    echo "✓ Cleaned up $removed_count auxiliary files"
else
    echo "✓ No auxiliary files to clean"
fi

echo ""
echo "======================================"
echo "Compilation completed successfully!"
echo "Output: book.pdf"
echo "======================================"

# Optional: Open PDF if on a system with a PDF viewer
if command -v xdg-open > /dev/null 2>&1; then
    read -p "Would you like to open the PDF? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        xdg-open book.pdf &
    fi
elif command -v open > /dev/null 2>&1; then  # macOS
    read -p "Would you like to open the PDF? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        open book.pdf &
    fi
fi