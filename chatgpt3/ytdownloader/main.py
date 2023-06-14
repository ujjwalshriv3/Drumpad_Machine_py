import yt_dlp as youtube_dl
import os


video_id = "dQw4w9WgXcQ"
video_url = "https://www.youtube.com/watch?v=" + video_id
# video_url = input("Enter the URL of the video you want to download: ")
dl_format = input(
    "What format do you want to download the video in? (a=audio/v=video) ")

if dl_format == "a":
    dirname = 'yt_downloads/audio/'
    # create the directory if it does not exist
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    ydl_opts = {
        'format': 'bestaudio/best',
        'hls_prefer_native': True,
        'outtmpl': dirname + '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }], }
elif dl_format == "v":
    dirname = 'yt_downloads/video/'
    # create the directory if it does not exist
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['en'],
        'prefer_ffmpeg': True,
        'hls_prefer_native': True,
        'outtmpl': dirname + '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mkv',
        }],
    }
else:
    print("Invalid input.")

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
