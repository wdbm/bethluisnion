#!/usr/bin/env python3
'''
################################################################################
#                                                                              #
# bethluisnion                                                                 #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program decodes a barcode or QR code from an image.                     #
#                                                                              #
# copyright (C) 2025 Will Breaden Madden, wbm@protonmail.ch                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses>.                                               #
#                                                                              #
################################################################################

usage:
    bethluisnion.py [options]

options:
    --imagefile=FILENAME   image filename
'''

import docopt

from PIL import Image
from pyzbar.pyzbar import decode

__version__ = "2025-07-24T2250Z"

def read_QR_code(image_path):
    '''
    Decode a barcode or QR code from an image.
    '''
    image = Image.open(image_path)
    decoded_objects = decode(image)
    if not decoded_objects:
        print(f"No code detected in {image_path!r}.")
        return
    for objects in decoded_objects:
        data = objects.data.decode('utf-8')
        print(f"Decoded data: {data}")

def main():
    options = docopt.docopt(__doc__)
    image_path = options['--imagefile']
    read_QR_code(image_path)

if __name__ == '__main__':
    main()
