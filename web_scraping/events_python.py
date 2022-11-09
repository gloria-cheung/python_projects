from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = Service("/Users/macuser/development/chromedriver")
chrome_driver_path.start()
driver = webdriver.Chrome(service=chrome_driver_path)

# find events on python.org and put into dictionary with time and title of each event
driver.get("https://www.python.org/")
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul li")
events_list = []
for event in events:
    events_list.append({"time": event.find_element(By.CSS_SELECTOR, "time").get_attribute("datetime")[:10], "name": event.find_element(By.CSS_SELECTOR, "a").text})

events_dictionary = {i: events_list[i] for i in range(len(events_list))}
print(events_dictionary)