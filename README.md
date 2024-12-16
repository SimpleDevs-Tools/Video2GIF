# Video 2 GIF

The following packages need to be installed:

- `moviepy==1.0.3`
    - Newer versions of `moviepy` do not have `moviepy.editor`, which is required for our scripts to work.
- `Pillow==9.5.0`
    - We must install `Pillow` version 9.5 due to an `ANTIALIAS` property that was removed after version `10.0.0`.

## Example Command

Basic Command:

```bash
python video2gif.py ./<INPUT_VIDEO_FILE>.mp4 <START_SEC> <END_SEC> -fps <INT> -w <INT>
```
