@echo off
setlocal enabledelayedexpansion

:: Check for Python installation and install if not present
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Installing Python...
    powershell "start ms-windows-store://pdp/?ProductId=9P7QFQMJRFP7"
    echo Please install Python from the store and rerun this script.
    exit /b
)

:: Check for virtual environment in the current directory
if not exist ".\venv\" (
    echo Creating virtual environment...
    python -m venv .\venv
    echo Virtual environment created.
) else (
    echo Virtual environment exists.
)

:: Activate the virtual environment
echo Activating virtual environment...
call .\venv\Scripts\activate
echo virtual environment activated.

echo Ueberpruefe installierte Python-Pakete...

:: Erstellen einer temporären Datei mit der Liste der installierten Pakete
echo Liste der installierten Pakete wird erstellt...
python -m pip list > temp_pip_list.txt
echo Liste der installierten Pakete wurde erfolgreich erstellt.

:: Liste der benötigten Pakete
set "packages=setuptools python-dotenv pyinstaller"

:: Überprüfen, ob Pakete installiert sind, und markieren von fehlenden Paketen
set "install_needed=false"
for %%i in (%packages%) do (
    findstr /C:"%%i" temp_pip_list.txt > nul
    if errorlevel 1 (
        echo [FEHLT] %%i
        set "install_needed=true"
    ) else (
        echo [OK] %%i ist installiert.
    )
)

:: Wenn Pakete fehlen, führen Sie die Installation aus
if "!install_needed!"=="true" (
    echo Einige Pakete fehlen. Beginne mit der Installation der fehlenden Pakete...
    python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --verbose %packages%
    if "!errorlevel!" == "0" (
        echo Alle fehlenden Pakete wurden erfolgreich installiert.
    ) else (
        echo Fehler bei der Installation einiger Pakete. Bitte ueberpruefen Sie die Protokolle.
    )
) else (
    echo Alle benoetigten Pakete sind bereits installiert. Keine Installation erforderlich.
)

:: Löschen der temporären Datei
del temp_pip_list.txt

:: Führen Sie Ihr Python-Skript aus. Ersetzen Sie 'Main.py' durch den Namen Ihres Skripts, falls anders.
echo Starte Python-Skript Main.py...
python "src\Main.py"

echo.
echo Skript wurde ausgefuehrt. Fenster schliessen oder weitere Befehle eingeben.
pause
