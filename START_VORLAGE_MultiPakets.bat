@echo off
setlocal enabledelayedexpansion

echo Ueberpruefe installierte Python-Pakete...

:: Erstellen einer temporären Datei mit der Liste der installierten Pakete
python -m pip list > temp_pip_list.txt
echo Liste der installierten Pakete wurde erfolgreich erstellt.

:: Liste der benötigten Pakete
set "packages=cx_Freeze setuptools python-dotenv pyinstaller"

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
    python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org %packages%
    if "!errorlevel!" == "0" (
        echo Alle fehlenden Pakete wurden erfolgreich installiert.
    ) else (
        echo Fehler bei der Installation einiger Pakete. Bitte überpruefen Sie die Protokolle.
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
