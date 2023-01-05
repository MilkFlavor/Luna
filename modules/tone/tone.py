"""
Feb 2020 - Nathan Cueto
Attempt to remove screentones from input images (png) using blurring and sharpening
"""

from logging import INFO, basicConfig, info
from os import listdir
import numpy as np
from cv2 import GaussianBlur, bilateralFilter, filter2D, imread, imwrite


basicConfig(format="[%(asctime)s] %(message)s", level=INFO)

info('----- ToneRemover modified by MilkFlavor -----')

def blur(img, blur_amount=5):
    """
    It takes an image and a blur amount, and returns a blurred image
    :param img: The image to be blurred
    :param blur_amount: The amount of blur to apply, defaults to 5 (optional)
    :return: the blurred image.
    """
    if blur_amount == 7 :
        dst2 = GaussianBlur(img,(7,7),0)
        dst = bilateralFilter(dst2, 7, 80, 80)
    else:
        dst2 = GaussianBlur(img,(5,5),0)
        dst = bilateralFilter(dst2, 7, 10 * blur_amount, 80)
    return dst

def sharp(img, sharp_point, sharp_low):
    """
    It takes an image, a sharpening point, and a sharpening low, and returns a sharpened image
    :param img: The image to be sharpened
    :param sharp_point: The point in the center of the kernel
    :param sharp_low: The value of the surrounding pixels
    :return: The sharpened image.
    """
    s_kernel = np.array([[0, sharp_low, 0], [sharp_low, sharp_point, sharp_low], [0, sharp_low, 0]])
    sharpened = filter2D(img, -1, s_kernel)
    return sharpened

def get_file_list(folder_dir):
    """
    It returns a list of files in the directory that end with .png, .PNG, .jpg, .JPG, or .jpeg.
    :param dir: The directory where the images are stored
    :return: A generator object.
    """
    return (i for i in listdir(folder_dir) if i.endswith('.png') or i.endswith('.PNG') or i.endswith('.jpg') or i.endswith('.JPG') or i.endswith('.jpeg'))

def remove_screentones(dir_i, dir_o, blur_amount, sh_point=5.56, sh_low=-1.14):
    """
    It takes an input directory, an output directory,
    a blur amount, a sharpness point, and a sharpness
    low, and then it removes the screentones from the
    images in the input directory and saves them to
    the output directory
    :param dir_i: input directory
    :param dir_o: output directory
    :param blur_amount: 1, 2, or 3
    :param sh_point: Sharpness of the image
    :param sh_low: -1.14
    """
    if(dir_i == [] or len(dir_i)==0):
        info('No input directory')
    if(dir_o == [] or len(dir_o)==0):
        info('No output directory')
    inputs = list(get_file_list(dir_i))
    if(len(inputs) == 0):
        info('No png file founded')

    info('Removing tone')

    sh_point = float(sh_point)
    sh_low = float(sh_low)
    sharps = (4 * sh_low) + sh_point - 1

    bs_amount = 0
    if(blur_amount==1):
        bs_amount=3
    if(blur_amount==2):
        bs_amount=5
    if(blur_amount==3):
        bs_amount=7

    for i in inputs:
        img = imread(dir_i + '/' + i)
        blurred = blur(img, bs_amount)
        ret = sharp(blurred, sh_point, sh_low)
        sucess = imwrite(dir_o + '/' + i, ret)
        if(sucess != True):
            info('An error occured')
    info('ToneRemover has done running')

dtext = ""
otext = ""

if __name__ == '__main__':
    d_entry = './input'
    o_entry = './output'
    filtslide = 2
    sharpSlide = 5.56
    shEntry = -1.14
    remove_screentones(d_entry, o_entry, filtslide, sharpSlide, shEntry)