import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-top-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


def get_recc_data():
    results = sp.current_user_top_tracks(limit=50, time_range='medium_term')
    results2 = sp.current_user_top_artists(limit=50, time_range="medium_term")

    top_attributes = {"artists": [], "tracks": [], "genres": sp.recommendation_genre_seeds()['genres']}

    for item in results["items"]:
        top_attributes["tracks"].append(((item['id']), item['popularity']))

    for item in results2["items"]:
        top_attributes["artists"].append(item['id'])

    top_attributes["tracks"] = [x[0] for x in sorted(top_attributes["tracks"], key=lambda tup: tup[1])[0: 2]]
    top_attributes["genres"] = random.sample(top_attributes["genres"], 2)
    top_attributes["artists"] = random.sample(top_attributes['artists'], 1)
    return top_attributes


def get_recommendations(top_attributes):
    result = sp.recommendations(limit=50, seed_artists=top_attributes['artists'],
                                seed_genres=top_attributes['genres'], seed_tracks=top_attributes['tracks'])
    sacred_table = []
    for track in result['tracks']:
        if len(track['artists']) > 1:
            artists = ', '.join([x['name'] for x in track['artists']])
        else:
            artists = track['artists'][0]['name']
        sacred_table.append([track['name'], track['popularity'], track['external_urls']['spotify']])
    return sacred_table
