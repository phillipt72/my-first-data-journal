@echo off
REM Build Script for Standalone Streamlit Dashboard (Windows)
REM This script builds a standalone executable of the dashboard using PyInstaller

echo =========================================
echo Building Standalone Streamlit Dashboard
echo =========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH!
    echo Please install Python 3 to build the executable.
    pause
    exit /b 1
)

echo [32m√[0m Python found
echo.

REM Check if virtual environment exists, create if not
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo [32m√[0m Virtual environment created
) else (
    echo [32m√[0m Virtual environment already exists
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo [32m√[0m Virtual environment activated
echo.

REM Install/upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip >nul 2>&1
echo [32m√[0m pip upgraded
echo.

REM Install requirements
echo Installing dependencies...
pip install -r requirements.txt
echo [32m√[0m Dependencies installed
echo.

REM Clean previous build
if exist "build" (
    echo Cleaning previous build...
    rmdir /s /q build
    if exist "dist" (
        rmdir /s /q dist
    )
    echo [32m√[0m Previous build cleaned
) else if exist "dist" (
    echo Cleaning previous build...
    rmdir /s /q dist
    echo [32m√[0m Previous build cleaned
)
echo.

REM Build with PyInstaller
echo Building executable with PyInstaller...
echo This may take several minutes...
echo.
pyinstaller dashboard.spec --clean

echo.
echo =========================================
echo Build Complete!
echo =========================================
echo.
echo The standalone executable can be found in:
echo   .\dist\DataJournalDashboard\
echo.
echo To run the dashboard:
echo   cd dist\DataJournalDashboard
echo   DataJournalDashboard.exe
echo.
echo To distribute:
echo   1. Compress the 'dist\DataJournalDashboard' folder
echo   2. Share the compressed file with users
echo   3. Users extract and run the executable - no Python needed!
echo.
pause
