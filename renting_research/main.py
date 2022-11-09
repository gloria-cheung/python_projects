import re
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def get_data():
    # create list of {address: x, price: y, link: z} from zillow website using beautiful soup
    response = requests.get("https://www.zillow.com/toronto-on/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-79.74030661914063%2C%22east%22%3A-79.01246238085938%2C%22south%22%3A43.47534133777822%2C%22north%22%3A43.93992968724773%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A2400%7D%2C%22price%22%3A%7B%22max%22%3A459330%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%7D", headers={"Accept-Language": "en-US,en;q=0.9", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup)
    items = soup.select(".result-list-container ul li") #  article div div.property-card-data

    properties_list = []

    for item in items:
        properties_list.append({
            "price": int(re.sub("\D", "", item.find(attrs={"data-test": "property-card-price"}).getText())),
            "link": item.select_one("a").get("href"),
            "address": item.select_one("address").getText()
        })
    return properties_list


def submit_form():
    # fill out google form that's linked to spreadsheet for each rental in list using selenium
    # https://forms.gle/avLBSnqfbQDU2fpD7
    pass


def email_link():
    # email link to spreadsheet to client (myself)
    pass


def automation():
    properties = get_data()
    submit_form()
    email_link()




