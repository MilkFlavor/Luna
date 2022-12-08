# Run yapf on all python files in the repo using pylintrc
# Usage: python scripts/pylint.py

import os


def main():
    print("If this script fails or runs into error please run:")
    print("pip install yapf")
    print("Then rerun this script\n")
    os.system("find . -type f -name "*.py" | xargs yapf -i")


if __name__ == "__main__":
    main()
