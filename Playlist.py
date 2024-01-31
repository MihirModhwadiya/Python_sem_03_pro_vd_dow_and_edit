from pytube import YouTube, Playlist
from moviepy.editor import *

def download_video(video_url, download_path):
    yt = YouTube(video_url)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution')[-1].download(download_path)
    print('Video Downloaded!')

def download_playlist(playlist_url, download_path):
    playlist = Playlist(playlist_url)
    for video_url in playlist.video_urls:
        download_video(video_url, download_path)

if __name__ == "__main__":
    while True:
        print("1. Download a single video")
        print("2. Download a playlist")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            video_url = input("Enter video link: ")
            download_path = "/yt_v/_lofi/"  # path of folder where you want to download your video
            download_video(video_url, download_path)
        elif choice == "2":
            playlist_url = input("Enter playlist link: ")
            download_path = "/yt_v/_lofi/"  # path of folder where you want to download your videos
            download_playlist(playlist_url, download_path)
        else:
            print("Invalid choice. Please enter 1 or 2.")
