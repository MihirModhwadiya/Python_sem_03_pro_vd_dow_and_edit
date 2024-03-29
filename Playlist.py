from pytube import YouTube, Playlist
from moviepy.editor import *
from multiprocessing import Pool

def download_video(video_url, download_path):
    yt = YouTube(video_url)
    yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution")[
        # 0 # highest resolution
        -1 # second highest 
        # -2 # thired highest

    ].download(download_path)
    print("Video Downloaded:", yt.title)


def download_playlist(playlist_url, download_path):
    playlist = Playlist(playlist_url)
    video_urls = playlist.video_urls
    with Pool(processes=4) as pool:
        pool.starmap(download_video, [(url, download_path) for url in video_urls])


if __name__ == "__main__":
    while True:
        print("1. Download a single video")
        print("2. Download a playlist")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            video_url = input("Enter video link: ")
            download_path = (
                "/yt_v/_soft_skills/"  # path of folder where you want to download your video
            )
            download_video(video_url, download_path)
        elif choice == "2":
            playlist_url = input("Enter playlist link: ")
            download_path = "/yt_v/_soft_skills/"  # path of folder where you want to download your videos
            download_playlist(playlist_url, download_path)
        else:
            print("Invalid choice. Please enter 1 or 2.")
