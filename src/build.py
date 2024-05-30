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
    # "excludes": ["tkinter"],  # Exclude any packages not needed
    "include_files": [
        os.path.join(os.path.dirname(__file__), "config.ini"),
        os.path.join(os.path.dirname(__file__), ".env"),
        (os.path.join(os.path.dirname(__file__), "Templates"), "Templates"),
        (os.path.join(os.path.dirname(__file__), "Data"), "Data"),
        (os.path.join(os.path.dirname(__file__), "Out"), "Out"),
        (os.path.join(os.path.dirname(__file__), "modules"), "modules")
    ]
}
# with GUI
# base = "Win32GUI" if sys.platform == "command" else None 

# without GUI
base = "Console"

setup(
    name="Test-Template_Repository",
    version="0.1",
    description="Testing exe with Template Repository",
    options={"build_exe": build_exe_options},
    executables=[Executable("Main.py", base=base)]
)
