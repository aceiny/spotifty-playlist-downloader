def get_playlist_id_from_url(url) : 
    try : 
        return url.split('/')[::-1][0].split('?')[0]
    except :
        return 'Not valid url'