from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = Service("/Users/macuser/development/chromedriver")
chrome_driver_path.start()
driver = webdriver.Chrome(service=chrome_driver_path)

# go to website and fill out signup form with first name, last name, email and should see success page
driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("gloria")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("cheung")

email = driver.find_element(By.NAME, "email")
email.send_keys("test@gmail.com")

submit_button = driver.find_element(By.CSS_SELECTOR, "button")
submit_button.click()

success_msg = driver.find_element(By.CSS_SELECTOR, "h1").text
print(success_msg == "Success!")
