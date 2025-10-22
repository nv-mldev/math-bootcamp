#!/bin/zsh

# Script to generate set operation diagrams

# Navigate to script directory
cd "$(dirname "$0")"

# Check if python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install it to continue."
    exit 1
fi

# Install dependencies if needed
echo "Installing dependencies..."
pip3 install -r requirements.txt

# Run the generation script
echo "Generating set operation diagrams..."
python3 generate_set_operations.py

echo "Done! The diagrams have been saved to ../book/figures/set_operations/"