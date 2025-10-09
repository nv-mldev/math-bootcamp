#!/bin/bash

# Generate puppeteer config based on OS
CONFIG_FILE="puppeteer-config.json"

# Detect OS and find Chrome executable
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    CHROME_PATHS=(
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        "/Applications/Chromium.app/Contents/MacOS/Chromium"
        "/usr/bin/chromium"
        "/usr/bin/google-chrome"
    )
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    CHROME_PATHS=(
        "/usr/bin/google-chrome"
        "/usr/bin/google-chrome-stable"
        "/usr/bin/chromium-browser"
        "/usr/bin/chromium"
        "/snap/bin/chromium"
        "/usr/bin/google-chrome-unstable"
    )
else
    # Windows or other
    CHROME_PATHS=(
        "/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
        "/mnt/c/Program Files (x86)/Google/Chrome/Application/chrome.exe"
        "chrome.exe"
        "chromium.exe"
    )
fi

# Find the first available Chrome executable
CHROME_EXEC=""
for path in "${CHROME_PATHS[@]}"; do
    if [[ -f "$path" ]]; then
        CHROME_EXEC="$path"
        break
    fi
done

# If no Chrome found, try which command
if [[ -z "$CHROME_EXEC" ]]; then
    CHROME_EXEC=$(which google-chrome 2>/dev/null || which chromium-browser 2>/dev/null || which chromium 2>/dev/null)
fi

if [[ -z "$CHROME_EXEC" ]]; then
    echo "Error: No Chrome/Chromium executable found!"
    echo "Please install Google Chrome or Chromium"
    exit 1
fi

echo "Found Chrome at: $CHROME_EXEC"

# Generate the config file with high-DPI support
cat > "$CONFIG_FILE" << EOF
{
    "executablePath": "$CHROME_EXEC",
    "args": [
        "--no-sandbox",
        "--disable-setuid-sandbox",
        "--disable-dev-shm-usage",
        "--no-first-run",
        "--no-zygote",
        "--single-process",
        "--disable-web-security",
        "--disable-features=VizDisplayCompositor",
        "--force-device-scale-factor=2",
        "--high-dpi-support=1",
        "--force-color-profile=srgb"
    ]
}
EOF

echo "Generated $CONFIG_FILE with Chrome path: $CHROME_EXEC"