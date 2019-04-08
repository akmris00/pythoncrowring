import pytube

yt = pytube.YouTube('https://www.youtube.com/watch?v=L-2M_-QLs8k')

videos = yt.streams.all()

print('videos', videos)

for i in range(len(videos)):
    print(i, ' , ', videos[i])

down_dir = "C:/Users/analysis/Desktop/youtube"

videos[0].download(down_dir)
