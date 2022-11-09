from selenium import  webdriver
from selenium.webdriver.chrome.service import Service


service = Service("/Users/macuser/development/chromedriver")
service.start()
driver = webdriver.Remote(service.service_url)

driver.get('http://www.amazon.ca/');