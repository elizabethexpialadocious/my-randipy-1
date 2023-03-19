# my-randipy-1
This is a cheap version of the excellent Randify https://github.com/tinyioda/Randify written in python. It does not modify the playlist in place but rather copies the songs to a new playlist in random order.

In order for this to work, you need to set up the various credentials needed as a Spotify developer; see https://developer.spotify.com/dashboard/

Specifically, you need:

1. `client_id`
1. `client_secret`
1. `redirect_uri`

from the Spotify developer dashboard. You also need:

* `user_id`

for the user whose playlist(s) you want to make a randomized version of. Normally this will be you and you kind fund your ID at https://developer.spotify.com/console/get-current-user/ (hint: mine is a long number but I'm not sure if that's universal).

Put those things in a `cred.py` file in the same folder as `randipy` and you should be good to go.

This script relies upon `spotipy` and `randomname`, so be sure to install those with `pip`. Good luck!
