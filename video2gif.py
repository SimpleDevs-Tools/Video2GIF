# Required packages:
# - moviepy
# - argparse

import argparse
import os
from moviepy.editor import VideoFileClip

def SubclipStartDuration(clip, start, duration):
    # Clip the provided clip starting from the start timestamp (seconds) upwards to the duration (seconds)
    subclip = clip.subclip(start, duration)
    return subclip 
  
def SubclipStartEnd(clip, start, end):
    # Clip the provided clip starting from the start timestamp (seconds) to the end timestamp (seconds)
    duration = end-start
    return SubclipStartDuration(clip, start, duration)

def SubclipStart(clip, start):
    # Clip the provided clip starting from the start timestamp (seconds) to the end of the video
    duration = clip.duration
    return SubclipStartDuration(clip, start, duration)

def SubclipEnd(clip, end):
    # Clip the provided clip starting from beginning to the end timestamp (seconds)
    return SubclipStartEnd(clip, 0, end)

def SubclipDuration(clip, duration):
    # Clip the provided clip starting from beginning upwards to the duration
    return SubclipStartDuration(clip, 0, duration)

parser = argparse.ArgumentParser(
    description='Convert videos to gifs',
    epilog="And that's how you'd foo a bar"
)
parser.add_argument('src', help="The video source file.")
parser.add_argument('start', 
                    help="The start timestamp (seconds) that we want to clip from.", 
                    type=float)
parser.add_argument('end',
                    help="The end timestamp (seconds) that we want to clip from.",
                    type=float)
parser.add_argument('-fps', '--frames_per_second',
                    help='The FPS of the output GIF. Can be used to speed up runtime operation',
                    type=int,
                    default=0)
parser.add_argument('-w', '--width',
                    help='The width of the output GIF. The height will be auto-calculated to match the output resolution',
                    type=int,
                    default=0)
args = parser.parse_args()

# generate the output filename based on basename and directory
basename = os.path.basename(args.src)
filename = os.path.splitext(basename)[0]
directory = os.path.dirname(args.src)
output_filepath = os.path.join(directory, filename+".gif")
print(f"Attempting to output GIF file as: {output_filepath}")

# generate a clip type from the video
clip = VideoFileClip(args.src).subclip(t_start=args.start, t_end=args.end)
fps = clip.fps
if args.frames_per_second > 0: 
    fps = args.frames_per_second
if args.width > 0:
    resized_clip = clip.resize(width=args.width)
    clip = resized_clip

# generate the clip
clip.write_gif(output_filepath, fps=fps, program='ffmpeg') 

# report
print(f"GIF file {output_filepath} successfully generated!")