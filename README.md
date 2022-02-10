# Generate Lottie JSON file

This script generates a Lottie JSON file from image sequences.


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
    -d image sequences location + pattern (ex: "./render/*.png") *1

  Optional args:
  -f Number of frames
  -o JSON file output location
  -n JSON file name
```

[1] ~Use quotes around the location ex `"./render/*.png"`~
[1] You may use `/path/to/images/*.png`
