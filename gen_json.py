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
from lottie.utils.script import script_main as generate_json
import glob

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
                    nargs='+',
                    required=True)


args = parser.parse_args()

# number of frames
frames = args.frames
# animation width and height (exported)
size = args.size
json_file_name = args.file_name
images_location = args.location

from generate import Anim
try:
    anim = Anim(frames=frames, size=size,
                images_location=images_location)
    anim = anim.get()
except ValueError as err:
    print(err)
    exit(1)

with patch.object(sys, 'argv', [sys.argv[0]]):
    generate_json(anim, path=args.output, basename=args.file_name, formats=['json'])
