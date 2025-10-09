#!/bin/bash

# Mermaid diagram converter script
# Usage: ./convert-mermaid.sh [input.mmd] [output.png/svg/pdf] [optional: format]

set -e

# Default values
INPUT_FILE=""
OUTPUT_FILE=""
FORMAT="png"
CONFIG_FILE="puppeteer-config.json"
WIDTH="2048"  # High resolution width
HEIGHT="1536" # High resolution height
SCALE="2"     # Device scale factor for high DPI

# Help function
show_help() {
    echo "Mermaid Diagram Converter"
    echo ""
    echo "Usage:"
    echo "  ./convert-mermaid.sh input.mmd output.png"
    echo "  ./convert-mermaid.sh input.mmd output.svg"
    echo "  ./convert-mermaid.sh input.mmd output.pdf"
    echo "  ./convert-mermaid.sh input.mmd  # outputs input.png"
    echo "  ./convert-mermaid.sh --all      # converts all .mmd files to PNG"
    echo ""
    echo "Options:"
    echo "  -h, --help     Show this help message"
    echo "  --all          Convert all .mmd files in current directory"
    echo "  --svg          Convert to SVG format"
    echo "  --pdf          Convert to PDF format"
    echo "  --hd           High resolution (2048x1536)"
    echo "  --4k           Ultra high resolution (3840x2160)"
    echo "  --custom WxH   Custom resolution (e.g., --custom 1920x1080)"
    echo ""
}

# Parse arguments
case "$1" in
    -h|--help)
        show_help
        exit 0
        ;;
    --all)
        echo "Converting all .mmd files to PNG..."
        for file in *.mmd; do
            if [[ -f "$file" ]]; then
                output="${file%.mmd}.png"
                echo "Converting $file -> $output (High Resolution: ${WIDTH}x${HEIGHT})"
                mmdc -i "$file" -o "$output" -p "$CONFIG_FILE" -w "$WIDTH" -H "$HEIGHT" -s "$SCALE"
            fi
        done
        exit 0
        ;;
    "")
        echo "Error: No input file specified"
        show_help
        exit 1
        ;;
    *)
        INPUT_FILE="$1"
        ;;
esac

# Check if input file exists
if [[ ! -f "$INPUT_FILE" ]]; then
    echo "Error: Input file '$INPUT_FILE' not found"
    exit 1
fi

# Determine output file and format
if [[ -n "$2" ]]; then
    OUTPUT_FILE="$2"
    # Extract format from extension
    case "$OUTPUT_FILE" in
        *.png) FORMAT="png" ;;
        *.svg) FORMAT="svg" ;;
        *.pdf) FORMAT="pdf" ;;
        *) 
            echo "Warning: Unknown output format, defaulting to PNG"
            FORMAT="png"
            ;;
    esac
else
    # Generate output filename from input
    OUTPUT_FILE="${INPUT_FILE%.mmd}.png"
fi

# Check for format and resolution flags
case "$2" in
    --svg) 
        OUTPUT_FILE="${INPUT_FILE%.mmd}.svg"
        FORMAT="svg"
        ;;
    --pdf)
        OUTPUT_FILE="${INPUT_FILE%.mmd}.pdf" 
        FORMAT="pdf"
        ;;
    --hd)
        OUTPUT_FILE="${INPUT_FILE%.mmd}_hd.png"
        WIDTH="2048"
        HEIGHT="1536"
        SCALE="2"
        ;;
    --4k)
        OUTPUT_FILE="${INPUT_FILE%.mmd}_4k.png"
        WIDTH="3840"
        HEIGHT="2160"
        SCALE="3"
        ;;
    --custom)
        if [[ -n "$3" && "$3" =~ ^[0-9]+x[0-9]+$ ]]; then
            WIDTH="${3%x*}"
            HEIGHT="${3#*x}"
            OUTPUT_FILE="${INPUT_FILE%.mmd}_${WIDTH}x${HEIGHT}.png"
            SCALE="2"
        else
            echo "Error: Invalid custom resolution format. Use --custom 1920x1080"
            exit 1
        fi
        ;;
esac

# Generate puppeteer config if it doesn't exist
if [[ ! -f "$CONFIG_FILE" ]]; then
    echo "Generating puppeteer config..."
    ./generate-puppeteer-config.sh
fi

# Convert the diagram
echo "Converting $INPUT_FILE -> $OUTPUT_FILE ($FORMAT format, ${WIDTH}x${HEIGHT}, scale: ${SCALE}x)"
mmdc -i "$INPUT_FILE" -o "$OUTPUT_FILE" -p "$CONFIG_FILE" -w "$WIDTH" -H "$HEIGHT" -s "$SCALE"

if [[ $? -eq 0 ]]; then
    echo "✓ Successfully converted to $OUTPUT_FILE"
    
    # Show file info
    if command -v ls &> /dev/null; then
        ls -lh "$OUTPUT_FILE"
    fi
else
    echo "✗ Conversion failed"
    exit 1
fi