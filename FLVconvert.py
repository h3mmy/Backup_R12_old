#!/usr/bin/env python

# Importing modules

import os

# Grabbing file list

lst = os.listdir('/Users/zachariahaslam/Downloads/Safari')

fnn = ''
ofnn = ''
com = 'ffmpeg -i '

for i in lst:
    if not (i == lst[0]):
        fnn = i
        ofnn = fnn.split('.')[0] + '.mp3'
        print com + fnn + ' ' + ofnn        # Stub - replace with os.system(com+...) when needed