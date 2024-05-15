@echo off
SetLocal EnableDelayedExpansion

echo Checking if Python is installed...

powershell -Command "& {
  $pythonPath = Get-Command python -ErrorAction SilentlyContinue
  if ($pythonPath) {
    $version = python --version
    Write-Output 'Python is installed: ' + $version
  } else {
    Write-Output 'Python is not installed, installing from Microsoft Store...'
    & winget install --id Python.Python.3 -e --source msstore
    Write-Output 'Python installation completed.'
  }
}"

echo Running the second script...
call Setup_script.bat

EndLocal
