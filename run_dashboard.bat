@echo off
REM Simple runner script for the Streamlit dashboard

echo Starting Data Journal Dashboard...
echo.
echo The dashboard will open in your default browser.
echo Press Ctrl+C to stop the server.
echo.

REM Check if streamlit is installed
streamlit --version >nul 2>&1
if errorlevel 1 (
    echo Error: Streamlit is not installed!
    echo.
    echo Please install dependencies first:
    echo   pip install -r requirements.txt
    echo.
    pause
    exit /b 1
)

REM Run streamlit
streamlit run dashboard.py
