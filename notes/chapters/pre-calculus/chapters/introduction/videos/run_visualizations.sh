#!/bin/bash

# Script to set up the environment and run the real line and modular arithmetic visualizations

# Colors for terminal output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Setting up environment for Real Line and Modular Arithmetic visualizations...${NC}"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Create a Python virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo -e "${BLUE}Creating virtual environment...${NC}"
    python3 -m venv venv
    echo -e "${GREEN}Virtual environment created.${NC}"
fi

# Activate the virtual environment
echo -e "${BLUE}Activating virtual environment...${NC}"
source venv/bin/activate

# Install required packages
echo -e "${BLUE}Installing required packages...${NC}"
pip install -q numpy matplotlib ipywidgets jupyter

# Optional: Install manim if user wants full animations
read -p "Do you want to install Manim for full animations? (y/n) " install_manim
if [[ $install_manim == "y" || $install_manim == "Y" ]]; then
    echo -e "${BLUE}Installing Manim...${NC}"
    pip install -q manim
    
    # Check if ffmpeg is installed (required for Manim)
    if ! command -v ffmpeg &> /dev/null; then
        echo "ffmpeg is required for Manim but is not installed."
        echo "Please install ffmpeg:"
        echo "  On macOS: brew install ffmpeg"
        echo "  On Ubuntu/Debian: sudo apt-get install ffmpeg"
    fi
    
    # Check if Cairo is installed (required for Manim)
    if ! python3 -c "import cairo" &> /dev/null; then
        echo "Cairo is required for Manim but is not installed."
        echo "Please install Cairo:"
        echo "  On macOS: brew install cairo"
        echo "  On Ubuntu/Debian: sudo apt-get install libcairo2-dev"
    fi
    
    echo -e "${GREEN}Manim installation completed.${NC}"
fi

# Options menu
echo -e "${BLUE}=== Real Line and Modular Arithmetic Visualizations ===${NC}"
echo "1) Run simple matplotlib visualizations"
echo "2) Open Jupyter notebook"
if [[ $install_manim == "y" || $install_manim == "Y" ]]; then
    echo "3) Run Manim animations"
fi
echo "q) Quit"

read -p "Enter your choice: " choice

case $choice in
    1)
        echo -e "${BLUE}Running simple matplotlib visualizations...${NC}"
        python3 simple_visualization.py
        ;;
    2)
        echo -e "${BLUE}Opening Jupyter notebook...${NC}"
        jupyter notebook real_line_and_modular.ipynb
        ;;
    3)
        if [[ $install_manim == "y" || $install_manim == "Y" ]]; then
            echo -e "${BLUE}Running Manim animations...${NC}"
            echo "Choose quality:"
            echo "l) Low quality (faster)"
            echo "m) Medium quality"
            echo "h) High quality (slower)"
            read -p "Enter quality choice: " quality
            
            case $quality in
                l) 
                    echo "Running low quality animation..."
                    python3 -m manim -pql real_line_and_modular.py RealLineAndModularArithmetic
                    ;;
                m)
                    echo "Running medium quality animation..."
                    python3 -m manim -pqm real_line_and_modular.py RealLineAndModularArithmetic
                    ;;
                h)
                    echo "Running high quality animation..."
                    python3 -m manim -pqh real_line_and_modular.py RealLineAndModularArithmetic
                    ;;
                *)
                    echo "Invalid choice. Using low quality."
                    python3 -m manim -pql real_line_and_modular.py RealLineAndModularArithmetic
                    ;;
            esac
        else
            echo "Manim is not installed. Please run the script again and choose to install Manim."
        fi
        ;;
    q|Q)
        echo -e "${GREEN}Exiting. Goodbye!${NC}"
        ;;
    *)
        echo "Invalid choice."
        ;;
esac

# Deactivate the virtual environment
deactivate
