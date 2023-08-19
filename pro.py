from tkinter.filedialog import *
from pytube import YouTube

''' pytube is a lightweight, dependency-free Python library which is used for downloading videos from the youtube. '''

from moviepy.editor import *

''' MoviePy is a Python module for video editing, which can be used for basic operations like cuts, concatenations, title insertions,
   video compositing, video processing, or to create advanced effects. It can read and write the most common video formats, including GIF. '''


'''Tkinter is the de facto way in Python to create Graphical User interfaces (GUIs) and is included in all standard Python Distributions.
   In fact, it's the only framework built into the Python standard library.
   The tkinter.filedialog module provides classes and factory functions for creating file/directory selection windows.'''


def menu():  # function to display menu
    print("\t\t\t---------------------------------")
    print("\t\t\t| 1. download youtube video.    |\n\t\t\t---------------------------------")
    print("\t\t\t| 2. convert video to audio.    |\n\t\t\t---------------------------------")
    print("\t\t\t| 3. make clip.                 |\n\t\t\t---------------------------------")
    print("\t\t\t| 4. make gif.                  |\n\t\t\t---------------------------------")
    print("\t\t\t| 5. make image.                |\n\t\t\t---------------------------------")
    print("\t\t\t| 6. concat video.              |\n\t\t\t---------------------------------")


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


def vid_to_aud():  # function to convert video to audio format
    vid = askopenfilename()
    video = VideoFileClip(vid)
    aud = video.audio
    a_name = input("Enter audio file name: ")  # asking for file name
    # path of folder where audio file will be saved
    aud.write_audiofile("/yt_v/_audio/" + a_name + ".mp3")


def make_clip():  # function to make subclip of video
    vid = askopenfilename()
    s1 = int(input("Enter first time: "))
    s2 = int(input("Enter second time: "))
    video = VideoFileClip(vid).subclip(s1, s2)
    a_name = input("Enter video file name: ")  # asking for file name
    # path of folder where clip will be saved
    video.write_videofile("/yt_v/_clip/" + a_name + ".mp4")


def gif_convert():  # function to convert subclip to gif (graphics interchange format)
    vid = askopenfilename()
    video = VideoFileClip(vid)
    a_name = input("Enter audio file name: ")  # asking for file name
    # path of folder where gif file will be saved
    video.write_gif("/yt_v/_gif/" + a_name + ".gif")


def image_convert():  # function to fetch image from video or subclip
    vid = askopenfilename()
    video = VideoFileClip(vid)
    a_name = input("Enter image file name: ")  # asking for file name
    tim = input("Enter time: ")
    # path of folder where image will be saved
    video.save_frame("/yt_v/_img/" + a_name + ".png", t=tim)


def video_concat():  # function to concat videos or sub clips
    vid1 = askopenfilename()
    vid2 = askopenfilename()
    video1 = VideoFileClip(vid1)
    video2 = VideoFileClip(vid2)
    video_cc = concatenate_videoclips([video1, video2])
    a_name = input("Enter video file name: ")  # asking for file name
    # path of folder where concat video will be saved
    video_cc.write_videofile("/yt_v/_concated/" + a_name + ".mp4")


# printing menu
print("\t\t\t---------------------------------")
print("\t\t\t| 1. download youtube video.    |\n\t\t\t---------------------------------")
print("\t\t\t| 2. convert video to audio.    |\n\t\t\t---------------------------------")
print("\t\t\t| 3. make clip.                 |\n\t\t\t---------------------------------")
print("\t\t\t| 4. make gif.                  |\n\t\t\t---------------------------------")
print("\t\t\t| 5. make image.                |\n\t\t\t---------------------------------")
print("\t\t\t| 6. concat video.              |\n\t\t\t---------------------------------")

ch = 'y'

while ch == 'y' or ch == 'Y':  # while loop for repetition of options

    # asking user for their choice
    ch = int(input("Enter which you choose (0. menu): "))

    if ch == 0:
        menu()  # calling function menu

    elif ch == 1:
        video_d()  # calling function video_d

    elif ch == 2:
        vid_to_aud()  # calling function vid_to_aud

    elif ch == 3:
        make_clip()  # calling function make_clip

    elif ch == 4:
        gif_convert()  # calling function gif_convert

    elif ch == 5:
        image_convert()  # calling function image_convert

    elif ch == 6:
        video_concat()  # calling function video_concat

    else:
        print("Invalid...")

    ch = input("you want to repeat? (y/n) :  ")  # asking user to repeat or not
