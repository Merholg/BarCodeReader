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


def get_barcode(filefullname):
    barcodes = list()
    flag = False
    if filefullname:
        flag = True
    while True:
        barcodes.clear()
        if not flag:
            fullname = input()
        else:
            fullname = filefullname
        if os.path.exists(fullname) and os.path.isfile(fullname):
            with Image.open(fullname) as im:
                barcodes = pyzbar.decode(im)
                if not (len(barcodes) > 0):
                    sharp_im = im.filter(ImageFilter.SHARPEN)
                    barcodes = pyzbar.decode(sharp_im)
            # dirname, filename = os.path.split(fullname)
            # relpath = dirname.replace(fullpath, "")
            i = 0
            if len(barcodes) > 0:
                # print("File {} barcode Found".format(image_file))
                for barcode in barcodes:
                    # print("barcode as: {}".format(barcode.data))
                    i += 1
                    print("{}\t{}\t{}\n".format(fullname, i, barcode.data.decode("utf-8")))
            else:
                # print("File {} barcode Not Found".format(image_file))
                print("{}\t{}\t{}\n".format(fullname, i, ""))
        else:
            # print("No {} exist or it is no file".format(fullname))
            print("{}\t{}\t{}\n".format("", 0, ""))
        if flag:
            break
    return


if len(sys.argv) < 2:
    # path = os.getcwd()
    imagefile_fullname = ""
else:
    imagefile_fullname = sys.argv[1]
    if '~' in imagefile_fullname:
        fullpath = os.path.expanduser(imagefile_fullname)
    else:
        fullpath = os.path.realpath(imagefile_fullname)
    if not (os.path.exists(imagefile_fullname) and os.path.isfile(imagefile_fullname)):
        imagefile_fullname = ""

sys.exit(get_barcode(imagefile_fullname))
