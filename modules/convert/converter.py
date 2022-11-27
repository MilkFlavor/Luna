"""
This script is used to convert the data from the old image format to a
PNG format by using the Pillow .save function.
"""
from os import mkdir, listdir, getcwd, path
from logging import basicConfig, info, INFO
from PIL import Image

basicConfig(format="[%(asctime)s] %(message)s", level=INFO)

def convert(input_path, output_path):
    """
    It takes in the input path and output path, creates the output folder 
    if it doesn't exist, and then converts each image in the input folder 
    to a PNG file and saves it in the output folder
    """
    try:
        # Create output folders
        mkdir(getcwd() + output_path)
        info(f"The output folder - {output_path}, has been created!")
    except FileExistsError:
        info(f"The folder {output_path} already exists! All the PNG files will be saved in it!")

    # Each image in the input folder is made into a .png
    for filename in listdir(getcwd() + input_path):
        current_img = Image.open(getcwd() + input_path + "/" + filename)
        info("Working on image: " + path.splitext(filename)[0])
        info(f"Format: {current_img.format}")
        info(f"Size: {current_img.size}")
        info(f"Mode: {current_img.mode}")
        current_img.save(
            getcwd() + output_path + "/" + path.splitext(filename)[0] + ".png", "PNG"
        )