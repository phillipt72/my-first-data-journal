#!/bin/bash
# Build Script for Standalone Streamlit Dashboard
# This script builds a standalone executable of the dashboard using PyInstaller

set -e  # Exit on error

echo "========================================="
echo "Building Standalone Streamlit Dashboard"
echo "========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed!"
    echo "Please install Python 3 to build the executable."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Check if virtual environment exists, create if not
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"
echo ""

# Install/upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip > /dev/null 2>&1
echo "✓ pip upgraded"
echo ""

# Install requirements
echo "Installing dependencies..."
pip install -r requirements.txt
echo "✓ Dependencies installed"
echo ""

# Clean previous build
if [ -d "build" ] || [ -d "dist" ]; then
    echo "Cleaning previous build..."
    rm -rf build dist
    echo "✓ Previous build cleaned"
    echo ""
fi

# Build with PyInstaller
echo "Building executable with PyInstaller..."
echo "This may take several minutes..."
echo ""
pyinstaller dashboard.spec --clean

echo ""
echo "========================================="
echo "Build Complete!"
echo "========================================="
echo ""
echo "The standalone executable can be found in:"
echo "  ./dist/DataJournalDashboard/"
echo ""
echo "To run the dashboard:"
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "  cd dist/DataJournalDashboard"
    echo "  DataJournalDashboard.exe"
else
    echo "  cd dist/DataJournalDashboard"
    echo "  ./DataJournalDashboard"
fi
echo ""
echo "To distribute:"
echo "  1. Compress the 'dist/DataJournalDashboard' folder"
echo "  2. Share the compressed file with users"
echo "  3. Users extract and run the executable - no Python needed!"
echo ""
