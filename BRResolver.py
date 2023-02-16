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
        barcodes.clear()
        fullname = input()
        if os.path.exists(fullname) and os.path.isfile(fullname):
            with Image.open(fullname) as im:
                barcodes = pyzbar.decode(im)
                if not (len(barcodes) > 0):
                    sharp_im = im.filter(ImageFilter.SHARPEN)
                    barcodes = pyzbar.decode(sharp_im)
            i = 0
            if len(barcodes) > 0:
                # print("File {} barcode Found".format(image_file))
                for barcode in barcodes:
                    # print("barcode as: {}".format(barcode.data))
                    i += 1
                    print("{}\t{}\t{}\t{}\n".format(filename, relpath.replace("/\\", ""), i,
                                                    barcode.data.decode("utf-8")))
            else:
                # print("File {} barcode Not Found".format(image_file))
                print("{}\t{}\t{}\t{}\n".format(filename, relpath.replace("/\\", ""), i, ""))
        else:
            # print("No {} exist or it is no file".format(fullname))
            print("")

    return


if __name__ == '__main__':
    if len(sys.argv) < 2:
        path = os.getcwd()
    else:
        path = sys.argv[1]

    if '~' in path:
        fullpath = os.path.expanduser(path)
    else:
        fullpath = os.path.realpath(path)

    sys.exit(get_barcode(fullpath))
