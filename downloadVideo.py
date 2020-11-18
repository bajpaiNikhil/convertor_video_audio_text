##video with  acodec="mp4a.40.2" can be downloaded with ssound attached



from pytube import YouTube
link =input("link:")

yt=YouTube(link)

video=yt.streams.all()

#print(videoo.first())
i=1
for stream in video:
    print(str(i)+"__"+str(stream))
    i+=1
stream_number=int(input("enter Number"))
# Prints something like "15.555% done..."
video=video[stream_number-1]
video.download("C:\\stupid")
# def progress_function(stream, chunk, file_handle, bytes_remaining):
#     print(round((1 - bytes_remaining / video.filesize) * 100, 3), '% done...')




print("working on it")





