from bs4 import BeautifulSoup
import requests


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

print(article_texts)
print(article_links)
print(article_upvotes)

max_upvote = max(article_upvotes)
article_idx = article_upvotes.index(max_upvote)
most_upvoted_article_text = article_texts[article_idx]
most_upvoted_article_link = article_links[article_idx]
print(f"The most upvoted article is: {most_upvoted_article_text} which can be found at {most_upvoted_article_link}")

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
# tags = soup.find_all(name="a")
# for tag in tags:
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading.text)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# company_url = soup.select_one(selector="p a") # can removve selector
# name = soup.select_one("#name")
# print(company_url)
# print(name)
#
# headings = soup.select(".heading")
# print(headings)