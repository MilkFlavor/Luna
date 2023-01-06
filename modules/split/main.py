"""
It takes all the files in the input folder, copies them to the output folder,
and then splits them
into two parts
"""
from logging import INFO, basicConfig, info
import os
import shutil
import lib

basicConfig(format="[%(asctime)s] %(message)s", level=INFO)

def main():
    """
    It takes all the files in the input folder, copies them to the output folder,
    and then splits them into two parts
    """
    info('----- Luna by Milkflavor -----')

    # Providing the folder path
    origin = os.getcwd() + '/input/'
    info(origin)
    target = os.getcwd() + '/output/'
    info(target)

    # Fetching the list of all the files
    files = os.listdir(origin)

    # Fetching all the files to directory
    for file_name in files:
        info("----- Copying... " + file_name + " -----")
        shutil.copy(origin+file_name, target+file_name)
    print("Files are copied successfully")

    os.chdir(target)

    for img in files:
        info("----- Splitting... " + img + " -----")
        lib.slice(img, 2)
        os.remove(img)
        info("----- " + img + " split successfully! -----")

if __name__ == '__main__':
    main()
