from pytube import YouTube
from youtubesearchpython import VideosSearch

def get_video_url_by_name(video_name):
    search = VideosSearch(video_name, limit = 1)
    results = search.result()

    if results:
        video_url = results['result'][0]['link']
        return video_url
    else:
        return "Video not found"


def download_youtube_audio(video_url):
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path='./audio')