import spotipy
from spotipy.oauth2 import SpotifyOAuth
import randomname
import random
import cred

auth=SpotifyOAuth(scope='playlist-modify-public',
                  client_id=cred.client_id,
                  client_secret=cred.client_secret,
                  redirect_uri=cred.redirect_uri)

sp = spotipy.Spotify(auth_manager=auth)

playlists = sp.user_playlists(cred.user_id)
my_copy = []

while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i  + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
        my_copy.append([playlist['uri'], playlist['name']])
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None

try:
    mode = int(input('Which playlist [1-' + str(len(my_copy)) + ']? '))
except ValueError:
    print("Not a number")
    SystemExit()

n = mode - 1
songs = sp.playlist_items(my_copy[n][0])
my_song_ids = []

print("Retrieving playlist '" + my_copy[n][1] + "' items.")

while songs:
    for i, song in enumerate(songs['items']):
        my_song_ids.append(song['track']['id'])
    if songs['next']:
        songs = sp.next(songs)
    else:
        songs = None

print("Playlist contains " + str(len(my_song_ids)) + " items.")

new_playlist_name = randomname.get_name()
print("New playlist name: " + new_playlist_name)

i = sp.user_playlist_create(user=cred.user_id, name=new_playlist_name)
new_playlist_id = i['id']
random.shuffle(my_song_ids)

limit = 100
for i in range(0, len(my_song_ids), limit):
    j = len(my_song_ids) if i + limit > len(my_song_ids) else i + limit
    print("Adding songs %d-%d of %d" % (i+1, j, len(my_song_ids)))
    sp.playlist_add_items(new_playlist_id, my_song_ids[i:i+limit])

