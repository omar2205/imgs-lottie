# Generate Lottie JSON file

<p align="center">
  <img src="https://user-images.githubusercontent.com/1373867/153498388-af085143-6242-4f58-926c-64d3a31c2b51.png" />
</p>

This script generates a Lottie JSON file from image sequences.


Frames: Number of frames, Size: Animation size (Format ex: 720x360)

Output: JSON output location

### Install

You need [Python3](https://www.python.org/downloads/)

1. Clone this repo or Code > DownloadZIP
2. Run `pip install -r requirement.txt`


### Usage

2 ways to run, GUI and CLI.

#### GUI

`python3 main.py`

#### CLI

```
gen_json.py
  Required args:
    -s size of animation (ex: 360x360)
    -d image sequences location + pattern (ex: "./render/*.png")

  Optional args:
  -f Number of frames
  -o JSON file output location
  -n JSON file name
```

