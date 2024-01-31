from pytube import YouTube
from moviepy.editor import *


def video_d():  # function to download YouTube video
    link = input("Enter video link: ")
    # video = v_name
    add = "/yt_v/_video/"  # path of folder where you want to download your video
    # ddata = pytube.YouTube(video)
    # DownloadVid = ddata.streams.get_highest_resolution()
    # DownloadVid.download(add)
    # print("Your video download is complete.")
    yt = YouTube(link)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution')[-1].download(add)
    print('Video Downloaded!')

while True:
    video_d()  # calling function video_d
