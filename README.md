# Video 2 GIF

This is a simple Python-based script for converting video clips into GIFs. This tool allows for some control over which parts of the video to convert and the outputted GIF's FPS and dimensions.

## Installation

After cloning this repo, ensure that these packages are installed. You may be required to create a separate environment for this, to prevent overriding existing package versions in your local machine.

- `moviepy==1.0.3`
    - Newer versions of `moviepy` do not have `moviepy.editor`, which is required for our scripts to work.
- `Pillow==9.5.0`
    - We must install `Pillow` version 9.5 due to an `ANTIALIAS` property that was removed after version `10.0.0`.

These can be easily installed via the `requirements.txt` script provided, via the following code:

```bash
pip install -r ./requirements.txt
```

## Commands

Generation of GIFs requires this simple command template:

```bash
python video2gif.py ./<INPUT_VIDEO_FILE>.mp4 <START_SEC> <END_SEC> -fps <INT> -w <INT>
```

**All outputs will be saved in the same directory as the provided input video, with the same filename**.

The arguments that can be passed are as follows:

|Argument|Required?|Type|Description|Default|
|:-:|:-:|:-:|:-|:-:|
|`src`|`true`|string|The video source file.||
|`start`|`true`|float|The start timestamp (in seconds) that we want to clip from.||
|`end`|`true`|float|The end timestamp (in seconds) that we want to clip from.||
|`-fps`, `--frames_per_second`|`false`|int|The FPS of the output GIF. Note that a higher FPS will increase processing time.|`15`|
|`-w`, `--width`|`false`|int|The width of the output GIF. The height will be auto-calculated to match the output resolution. By default (`0`), the outputted GIF will match the original video width.|`0`|

An example is provided in `./samples/sample.mp4`, which is a 1024x1024 video @ 30 FPS that is 55 seconds long. The command below will produce a GIF that is 512x512px at 15 FPS, from 00:10 to 00:20.

```bash
python video2gif.py ./samples/sample.mp4 10 20 -fps 15 -w 512
```