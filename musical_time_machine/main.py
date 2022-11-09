import os
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv


def get_data(date):
    # scraping to get list of song titles for year
    response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find("div", class_="chart-results-list").select("div ul li ul li h3", id="title-of-a-story")

    # reformatting the song title and removing unneeded chars
    return [item.getText().replace("\n", "").replace("\t", "") for item in titles]


def authenticate():
    # get keys from .env to use for authentication to spotify using spotipy
    load_dotenv()
    SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
    SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
    SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

    # authentication
    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private", client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI))


def get_song_uris(titles, sp, year):
    # list of song URIs
    song_uri_list = []
    for title in titles:
        # try to see if track is available on spotify, if not will just skip over that song title
        try:
            result = sp.search(q=f"year: {year} track: {title}", type="track")["tracks"]["items"][1]["uri"]
            song_uri_list.append(result)
        except IndexError:
            continue
    return song_uri_list


def start():
    date = input("Which year do you want to travel to? Type the date in the format of YYYY-MM-DD: ")
    year = date[:4]

    print(f"Fetching songs from {date}...")
    song_titles_list = get_data(date)
    sp = authenticate()

    current_user_id = sp.current_user()["id"]
    song_uri_list = get_song_uris(song_titles_list, sp, year)

    print("Creating private playlist on Spotify...")
    new_playlist = sp.user_playlist_create(user=current_user_id, name=f"{date} Billboard 100", public=False)
    sp.playlist_add_items(playlist_id=new_playlist["id"], items=song_uri_list)

    print("Playlist created! Check it out on spotify")


start()
