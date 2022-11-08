from bs4 import BeautifulSoup
import requests

# date = input("Which year do you want to travel to? Type the date in the format of YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/2000-08-12")
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find("div", class_="chart-results-list").select("div ul li ul li h3",id="title-of-a-story")
song_titles_list = [item.getText().replace("\n", "").replace("\t", "") for item in titles]
print(song_titles_list)