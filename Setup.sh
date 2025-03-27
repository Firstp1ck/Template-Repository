#!/bin/bash

# Check for Python installation and install if not present
if ! command -v python3 &> /dev/null
then
    echo "Python is not installed. Installing Python..."
    sudo pacman -Syu
    sudo pacman -S python --noconfirm
    echo "Python has been installed. Please rerun this script."
    exit 1
fi

# Check for virtual environment in the current directory
if [ ! -d "./venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv ./venv
    echo "Virtual environment created."
else
    echo "Virtual environment exists."
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source ./venv/bin/activate
echo "Virtual environment activated."

echo "Checking installed Python packages..."

# Create a temporary file with the list of installed packages
echo "Creating list of installed packages..."
pip list > temp_pip_list.txt
echo "List of installed packages created successfully."

# List of required packages
packages=("setuptools" "python-dotenv" "pyinstaller")

# Check if packages are installed and mark missing packages
install_needed=false
for package in "${packages[@]}"; do
    if ! grep -q "$package" temp_pip_list.txt; then
        echo "[MISSING] $package"
        install_needed=true
    else
        echo "[OK] $package is installed."
    fi
done

# If packages are missing, perform the installation
if [ "$install_needed" = true ]; then
    echo "Some packages are missing. Starting installation of missing packages..."
    pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --verbose "${packages[@]}"
    if [ $? -eq 0 ]; then
        echo "All missing packages were successfully installed."
    else
        echo "Error installing some packages. Please check the logs."
    fi
else
    echo "All required packages are already installed. No installation needed."
fi

# Delete the temporary file
rm temp_pip_list.txt

echo
echo "Script executed. Close the window or enter further commands."