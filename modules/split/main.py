# importing the modules
import os
import shutil
import lib

# Providing the folder path
origin = os.getcwd() + '/input/'
print (origin)
target = os.getcwd() + '/output/'
print (target)

# Fetching the list of all the files
files = os.listdir(origin)

# Fetching all the files to directory
for file_name in files:
    shutil.copy(origin+file_name, target+file_name)
print("Files are copied successfully")

os.chdir(target)

for x in files:
    lib.slice(x, 4)
    os.remove(x)
