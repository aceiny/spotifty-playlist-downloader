from sptf import get_playlist_tracks
from ytb import get_video_url_by_name, download_youtube_audio

playlist_id = input('Enter playlist id: ')

playlist_tracks = get_playlist_tracks(playlist_id)

for track in playlist_tracks:
    try :
        video_url = get_video_url_by_name(track)
        download_youtube_audio(video_url)
        print('downloaded ' + track)
    except:
        print('Error')
        continue