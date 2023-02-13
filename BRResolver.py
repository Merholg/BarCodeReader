#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  BRResolver.py
#
#  Copyright 2022 mc <mc@PyBuntu>
import sys
import os
from PIL import Image, ImageFilter
from pyzbar import pyzbar


def get_barcode(args):
    barcodes = list()
    while True:
        fullname = input()
        if os.path.exists(fullname) and os.path.isfile(fullname):
            filename = os.path.basename(fullname)
            name, ext = os.path.splitext(filename)
            try:
                with Image.open(fullname) as im:
                    barcodes = pyzbar.decode(im)
                    if not (len(barcodes) > 0):
                        sharp_im = im.filter(ImageFilter.SHARPEN)
                        barcodes = pyzbar.decode(sharp_im)
            except OSError as os_error:
                print("Error open image as: {} because: {}".format(fullname, os_error))
                return barcodes
            except ValueError as val_error:
                print("Format could not be determined from the file as: {} because: {}".format(fullname, val_error))
                return barcodes
        # except:
        #     print("Another error or warning: {}".format(fullname))
        #     return barcodes
        else:
            # print("No {} exist or it is no file".format(fullname))


    return


if __name__ == '__main__':
    sys.exit(get_barcode(sys.argv))
