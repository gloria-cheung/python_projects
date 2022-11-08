from bs4 import BeautifulSoup

# using beautiful soup to scrape data from website.html
with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
tags = soup.find_all(name="a")
for tag in tags:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading.text)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a") # can removve selector
name = soup.select_one("#name")
print(company_url)
print(name)

headings = soup.select(".heading")
print(headings)