from pytube import YouTube
import os
import ffmpeg
import subprocess
import time

a = True

while a:
    url = input("URL: ")

    if url == False:
        a = False
    # Title and Time
    print("...")
    print(((YouTube(url)).title))
    print("...")

    # Filename specification
    # Prevents any errors during conversion due to illegal characters in name
    _filename = input("Filename and format: ")

    # Downloading
    print("Downloading....")
    YouTube(url).streams.get_highest_resolution().download(filename=_filename)
    time.sleep(1)

    # Converting
    mp4 = "'%s'.mp4" % _filename
    mp3 = "'%s'.mp3" % _filename
    formateiro = ("ffmpeg %s " % mp4 + mp3)
    subprocess.run(formateiro, shell=True)

    # Completion
    print("\nCOMPLETE\n")