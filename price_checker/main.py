import os

from bs4 import BeautifulSoup
import requests
from smtplib import SMTP
from dotenv import load_dotenv

response = requests.get("https://ca.camelcamelcamel.com/product/B083S6Q8VK", headers={"Accept-Language": "en-US,en;q=0.9", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"})

soup = BeautifulSoup(response.text, "html.parser")
price = float(soup.select_one("span span", class_="green").getText()[1:])
title = soup.select_one("h2 a").getText()
link_to_amazon = soup.select_one("p a").get("href")


def send_email():
    load_dotenv()
    email = os.getenv("email")
    password = os.getenv("password")

    server = SMTP("smtp.gmail.com", port=587)
    server.starttls()
    server.login(email, password)
    SMTP.sendmail(self=server, from_addr="gloriacheung812@smtp.gmail.com", to_addrs="gloriacheung812@gmail.com", msg="Subject: Amazon Price Alert\n\n{} is now ${}. \n\n{}".format(title, price, link_to_amazon))


if price < 69.99:
    send_email()