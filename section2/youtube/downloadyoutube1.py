import pytube
import os
import subprocess

VNum = input("영상 주소? ")
yt = pytube.YouTube(VNum)

videos = yt.streams.all()

print('videos', videos)

for i in range(len(videos)):
    print(i, ' , ', videos[i])

CNum = int(input("화질 선택? "))

down_dir = "C:/Users/analysis/Desktop/youtube"

videos[CNum].download(down_dir)

newFileName = input('변환할 파일명? ')
oriFileName = videos[CNum].default_filename

subprocess.call(['ffmpeg','-i',
    os.path.join(down_dir,oriFileName),
    os.path.join(down_dir,newFileName)
])
