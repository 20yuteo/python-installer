from yt_dlp import YoutubeDL

import sys
import glob
import os
import subprocess

args = sys.argv
link = args[1]

ydl = YoutubeDL()
ydl.download([link])

videos = glob.glob('./*.mp4')

for video in videos:
    os.rename(video, video.replace(' ', ''))
    
videos = glob.glob('./*.mp4')

count = 0

for video in videos:
    size = os.path.getsize(video)
    if size>1000000000:

        subprocess.call('ffmpeg -i '+video+' -crf 18 '+video[:-3]+'_圧縮済.mp4', shell=True)

        os.rename(video, './'+str(count)+'_圧縮前_'+video[2:])
        count += 1