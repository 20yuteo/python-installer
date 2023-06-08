from yt_dlp import YoutubeDL

import sys

args = sys.argv
link = args[1]

ydl = YoutubeDL()
result = ydl.download([link])