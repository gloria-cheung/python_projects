import os
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# get keys from .env to use for authentication to spotify using spotipy
load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

# authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private", client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI))
current_user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in the format of YYYY-MM-DD: ")
year = date[:4]

#scraping to get list of song titles for year
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find("div", class_="chart-results-list").select("div ul li ul li h3", id="title-of-a-story")

# reformatting the song title and removing uneeded chars
song_titles_list = [item.getText().replace("\n", "").replace("\t", "") for item in titles]

# list of song URIs
song_URIs = []
for title in song_titles_list:
    # try to see if track is available on spotify, if not will just skip over that song title
    try:
        result = sp.search(q=f"year: {date} track: {title}", type="track")["tracks"]["items"][0]["album"]["uri"]
        song_URIs.append(result)
    except IndexError as e:
        continue

