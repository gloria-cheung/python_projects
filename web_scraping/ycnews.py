from bs4 import BeautifulSoup
import requests


# using beautiful soup to scrape data from news website to find most upvoted article from list of top 30
response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all("span", class_="titleline")
upvotes = soup.find_all("span", class_="score")

article_texts = []
article_links = []
article_upvotes = [int(upvote.getText().split(" ")[0]) for upvote in upvotes]

for article in articles:
    article_texts.append(article.find("a").getText())
    article_links.append(article.find("a").get("href"))

# print(article_texts)
# print(article_links)
# print(article_upvotes)

max_upvote = max(article_upvotes)
article_idx = article_upvotes.index(max_upvote)
most_upvoted_article_text = article_texts[article_idx]
most_upvoted_article_link = article_links[article_idx]
print(f"The most upvoted article is: {most_upvoted_article_text} which can be found at {most_upvoted_article_link}")
