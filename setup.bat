@echo off
echo Setting up the project environment...
echo =============================

REM Check for Python installation
python --version
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python before proceeding.
    pause
    exit /b
)

REM Install required Python modules
echo Installing required modules...
pip install selenium
pip install pillow

REM Confirm success
echo =============================
echo All dependencies have been installed successfully!
echo You can now run the Python script.
pause