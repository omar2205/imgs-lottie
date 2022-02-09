#!/usr/bin/python3
# Create a Lottie json file from an image sequence
# copyright (c) 2022
# oskr.nl - v0.1b

# Usage:
# gen_json.py
#   -o JSON file output location
#   -n JSON file name
#   -f Number of frames
#   -s size of animation (ex: 360x360)
#   -d image sequences location + pattern (ex: ./render/*.png)

import sys
import glob
from lottie.utils import script
from lottie import objects

import argparse
try:
    from unittest.mock import patch # type: ignore
except ImportError:
    from mock import patch # type: ignore

parser = argparse.ArgumentParser()
parser.add_argument('-o', 
                    dest='output', 
                    help='JSON file output location',
                    default='.')
parser.add_argument('-f', 
                    dest='frames', 
                    help='Number of frames',
                    type=int,
                    default=60)
parser.add_argument('-n', 
                    dest='file_name', 
                    help='JSON file file name (no .json)',
                    default='my_animation')
parser.add_argument('-s', 
                    dest='size', 
                    help='Width x height (ex: 720x360)',
                    required=True)
parser.add_argument('-d', 
                    dest='location', 
                    help='image sequences location + pattern (ex: ./*.png)',
                    required=True)


args = parser.parse_args()

# number of frames
frames = args.frames
# animation width and height (exported)
size = args.size.split('x')
width = size[0]
height = size[1]
json_file_name = args.file_name

# Create an Animation
anim = objects.Animation(frames)
anim.width = width
anim.height = height

# Get a list of all *.png images in current dir
files = glob.glob(args.location)

# we create a layer for every image
for idx, img_file in enumerate(files):
    # load an image and add it to our assets
    img = objects.assets.Image().load(img_file)
    anim.assets.append(img)

    # create an image layer with the image id
    layer = objects.ImageLayer(img.id)
    # add it to our animation
    p = anim.add_layer(layer)
    # start and in and out times (from our index)
    p.start_time = idx
    p.in_point = idx        # type: ignore
    p.out_point = idx + 1   # type: ignore

with patch.object(sys, 'argv', [sys.argv[0]]):
    script.script_main(anim, path=args.output, basename=args.file_name, formats=['json'])
