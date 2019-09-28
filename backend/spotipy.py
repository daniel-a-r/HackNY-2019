import spotipy
import sys
import spotipy.util as util

#util.prompt_for_user_token(username,scope = 'user-library-read',client_id='c78f678210dc4b199fbd20595064b0fa',client_secret='f3f26c184a6544b8b28fc9645c64f17a',redirect_uri='http://example.com/callback/?code=AQCcngI86gv2gmsF85UQDbyiR91hoEKY4UfbEHfLKsg9srYJ1AeOcUc44e6DgEbC0QUWCn8J1wCT1mCMTQ6jjcYjdJqR_OLbOYHCMi6V_CKGsIbUOgpaJ-y_yLcqi_6AF71P3D5eYQskrjh_cFl7_Q0XVMNx-6I1pyfE3RiRIRJPhbp2MUpTTtLFNJBvpC63QIcf91r3Q5iMP3ugDLbbeB2Bt0aO7A3B59nYWw')

SPOTIPY_CLIENT_ID = 'c78f678210dc4b199fbd20595064b0fa'
SPOTIPY_CLIENT_SECRET = 'f3f26c184a6544b8b28fc9645c64f17a'
SPOTIPY_REDIRECT_URI = 'http://google.com/'

#Get the username
#username = input("enter your username: ")
#scope is for what the user is currently playing
scope = 'user-read-currently-playing'
username = 'willptacek'

token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

spotifyObject = spotipy.Spotify(auth=token)

current_track = spotifyObject.current_user_playing_track() #gets current track from user

print(type(current_track))

print("Artist = " + current_track['item']['album']['artists'][0]['name'])
print("Song = " + current_track['item']['name'])
print("Album = " + current_track['item']['album']['name'])
