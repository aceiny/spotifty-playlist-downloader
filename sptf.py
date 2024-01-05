import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '59238d4dbcda4cf6a06bbf0f4ebeddfb'
client_secret = '141c33ef50b044699465be00dc25ed02'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

def get_playlist_tracks(playlist_id):
    l = []
    offset = 0

    while True:
        results = sp.playlist_tracks(playlist_id, offset=offset)
        if not results or not results.get('items'):
            break

        for track in results['items']:
            if track and track.get('track') and track['track'].get('artists') and track['track']['artists']:
                l.append(track['track']['artists'][0]['name'] + ' - ' + track['track']['name'])

        offset += len(results['items'])

    return l


