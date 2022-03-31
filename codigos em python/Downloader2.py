from pytube import YouTube

link = "https://www.youtube.com/watch?v=L6Dx9ZcgiDc"

yt = YouTube(link)  

try:
    yt.streams.get_highest_resolution().download(output_path = ".", filename = "Reiner and Bertholdt Transformation scene.mp4")
except:
    print("Some Error!")
print('Task Finished!')