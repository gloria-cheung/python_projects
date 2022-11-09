import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def load_page():
    chrome_driver_path = Service("/Users/macuser/development/chromedriver")
    chrome_driver_path.start()
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=chrome_driver_path, options=chr_options)
    # open page and wait for popup language selector, close cookie declaration and open stats
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    time.sleep(3)
    driver.find_element(By.ID, "langSelect-EN").click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Got it!").click()
    driver.find_element(By.ID, "statsButton").click()
    return driver


def play(driver):
    cookie = driver.find_element(By.ID, "bigCookie")
    play_for = 300
    begin = time.time()
    # play game for total of 5 min
    while time.time() - begin < play_for:
        # every 5 seconds, check what upgrade can be purchased
        period = 5
        start = time.time()

        while time.time() - start < period:
            cookie.click()

        upgrades = driver.find_elements(By.CSS_SELECTOR, ".upgradeBox div.crate")
        if len(upgrades) > 0:
            upgrades[0].click()

        store = driver.find_elements(By.CSS_SELECTOR, "#products div.enabled.unlocked")
        if len(store) > 0:
            store[len(store) - 1].click()


def start():
    driver = load_page()
    play(driver)

    time.sleep(5)
    print(driver.find_element(By.ID, "statsGeneral").find_elements(By.CSS_SELECTOR, "div.listing")[5].text)


start()