# importing the modules
from logging import INFO, basicConfig, info
import os
import shutil
import lib

basicConfig(format="[%(asctime)s] %(message)s", level=INFO)

info('----- Luna by Milkflavor -----')

# Providing the folder path
origin = os.getcwd() + '/input/'
info(origin)
target = os.getcwd() + '/output/'
info (target)

# Fetching the list of all the files
files = os.listdir(origin)

# Fetching all the files to directory
for file_name in files:
    file_folder = target+file_name
    # make a folder for each file
    os.mkdir(file_folder)
    info(file_name)
    shutil.copy(origin+file_name, file_folder)
info("Files are copied successfully")

os.chdir(target)

for x in files:
    info(f'----- Starting {x} -----')
    os.chdir(target+x)
    lib.slice(x, 2)
    os.remove(x)
    info(f'----- Finished {x} -----')

info('----- Done -----')
