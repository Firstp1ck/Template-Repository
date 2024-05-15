@echo off
REM Check for Python and install virtual environment
where python
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH.
    goto end
)

REM Create virtual environment
python -m venv venv
echo Created virtual environment.

REM Activate the virtual environment
call venv\Scripts\activate.bat
echo Activated virtual environment.

REM Install dependencies
pip install -r requirements.txt
echo Installed requirements.

:end
echo Setup complete.
pause
