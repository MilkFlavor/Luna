"""
Feb 2020 - Nathan Cueto
Main function for UI and uses Detector class
"""

import warnings

warnings.filterwarnings('ignore')

import os
from logging import info

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import configparser
import sys

from detector import Detector

versionNumber = '1.6.9'
weights_path = 'weights.h5'
cfg_path = '/content/Luna/hconfig.ini'

info('----- HentAI modified by MilkFlavor -----')


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def hentAI_detection(dcp_dir=None,
                     in_path=None,
                     is_mosaic=False,
                     is_video=False,
                     dilation=0):

    if dcp_dir is None:
        info('Input directory not founded')
    if in_path is None:
        info('Onput directory not founded')

    hconfig = configparser.ConfigParser()
    hconfig.read(cfg_path)
    if 'USER' in hconfig:
        hconfig['USER']['dcpdir'] = dcp_dir
        hconfig['USER']['srcdir'] = in_path
        hconfig['USER']['gmask'] = str(dilation)
    else:
        info("ERROR in hentAI_detection: Unable to read config file")
    with open(cfg_path, 'w') as cfgfile:
        hconfig.write(cfgfile)

    dilation = (dilation) * 2

    if (is_mosaic == True and is_video == False):
        info('Mosaic detection not supported')

    if (is_video == True):
        info('Video detection not supported')
    else:
        info('----- Running detection -----')
        detect_instance.run_on_folder(input_folder=in_path,
                                      output_folder=dcp_dir + '/',
                                      is_video=False,
                                      is_mosaic=is_mosaic,
                                      dilation=dilation)

    detect_instance.unload_model()
    info('Process complete')


def bar_detect():
    d_entry = 'output'
    o_entry = 'input'
    dil_entry = 3
    hentAI_detection(dcp_dir=d_entry,
                     in_path=o_entry,
                     is_mosaic=False,
                     is_video=False,
                     dilation=int(dil_entry))


if __name__ == "__main__":
    detect_instance = Detector(weights_path=weights_path)
    bar_detect()
