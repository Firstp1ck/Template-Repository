@echo off
:: Überprüfen, ob die Pakete bereits installiert sind
goto :SKIP
python -m pip list | findstr /C:"PAKET" > nul

:: Wenn das Paket nicht gefunden wurde, führe die Installation aus
if errorlevel 1 (
    echo Paket 'PAKET' wird installiert...

    python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org PAKET

) else (
    echo Pakete sind bereits installiert.
)
:SKIP
:: Führen Sie Ihr Python-Skript aus. Ersetzen Sie 'Main.py' durch den Namen Ihres Skripts.
:: python Main.py
python .\module_name\config.py

echo.
echo Skript wurde ausgefuehrt. Fenster schliessen oder weitere Befehle eingeben.
pause

