#!/bin/bash
# Simple runner script for the Streamlit dashboard

echo "Starting Data Journal Dashboard..."
echo ""
echo "The dashboard will open in your default browser."
echo "Press Ctrl+C to stop the server."
echo ""

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "Error: Streamlit is not installed!"
    echo ""
    echo "Please install dependencies first:"
    echo "  pip install -r requirements.txt"
    echo ""
    exit 1
fi

# Run streamlit
streamlit run dashboard.py
