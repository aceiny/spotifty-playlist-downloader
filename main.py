from sptf import get_playlist_tracks
from ytb import get_video_url_by_name, download_youtube_audio
from url import get_playlist_id_from_url

playlist_url = input('Enter playlist url: ')

playlist_id = get_playlist_id_from_url(playlist_url)

if playlist_id == 'Not valid url':
    print('Not valid url')
    exit()

playlist_tracks = get_playlist_tracks(playlist_id)

for track in playlist_tracks:
    try :
        video_url = get_video_url_by_name(track)
        download_youtube_audio(video_url)
        print('downloaded ' + track)
    except:
        print('Error')
        continue
    