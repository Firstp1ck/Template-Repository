from cx_Freeze import setup, Executable
import os
import sys

def load_requirements(path):
    """ Load requirements from a requirements.txt file. """
    with open(path, 'r') as file:
        return [line.strip() for line in file if line.strip() and not line.startswith('#')]

# Load packages from requirements.txt, excluding any version info
packages = load_requirements("requirements.txt")
packages = [pkg.split('==')[0] for pkg in packages]  # This removes version constraints, adjust if needed

build_exe_options = {
    "packages": packages,  # All packages from requirements.txt
    "excludes": ["tkinter"],  # Exclude any packages not needed
    "include_files": [
        os.path.join(os.path.dirname(__file__), "config.ini"),
        (os.path.join(os.path.dirname(__file__), "Templates"), "Templates"),
        (os.path.join(os.path.dirname(__file__), "Data"), "Data")
    ]
}

base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="YourAppName",
    version="0.1",
    description="Your Application Description",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)
