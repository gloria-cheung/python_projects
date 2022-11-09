from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = Service("/Users/macuser/development/chromedriver")
chrome_driver_path.start()
driver = webdriver.Chrome(service=chrome_driver_path)

# get num articles from wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a").text
print(article_count)

# type in search bar, hit enter and loads new page
search = driver.find_element(By.NAME, "search")
search.send_keys("Python", Keys.ENTER)
print(driver.find_element(By.LINK_TEXT, "Python (programming language)").text)