"""
Running the isort command on the source_dirs.
"""
import subprocess
from logging import info

print("If this script fails or runs into error please run:")
print("Ubuntu: sudo apt install isort")
print("Arch: sudo pacman -S isort")
print("Mac: pip install isort")
print("Windows: pip install isort")
print("Then rerun this script\n")

source_dirs = "modules scripts"
subprocess.check_call(f"isort {source_dirs}", shell=True)
info("isort done")
