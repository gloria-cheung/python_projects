from bs4 import BeautifulSoup
import requests


# using beautiful soup to web scrape data from {url} and save each movie (starting from 1 -> 100) to movies.txt file
# url => https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_page = response.text
soup = BeautifulSoup(movies_page, "html.parser")
titles = soup.find_all("h3", class_="title")

# create new list of titles and use text within the h3 tags as each item in list
movie_titles_list = [item.getText() for item in titles]
movie_titles_list.reverse()
text = "\n".join(movie_titles_list)

with open("movies.txt", "w") as file: #if file exists, will override the file with this: if doesnt exist, will create
    file.write(text)