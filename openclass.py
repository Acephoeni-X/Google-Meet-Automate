import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import requests
from datetime import datetime

def exitprogram(driver):
    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div')))
    element.click()
    driver.close()


def automate(driver, link):
    #driver = webdriver.chrome(driver)
    driver.get(link)
    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span')))
    element.click()
    # wait = WebDriverWait(driver, 20)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span')))
    element.click()

    #Send Message to Telegram:-
    url = f'https://api.telegram.org/bot1532806948:AAHrR1O49Ow4J06-nVBqNo9I8XtFHmHLXGI/sendMessage?chat_id=-562221071&text="Hello"'
    requests.get(url)

    while True:
        now = datetime.now()
        current = now.strftime("%H:%M")
        if (str(current)=='23:01'):
            requests.get(url)
            # element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div/span/span/svg')))
            # element.click()
            # break
            exitprogram(driver)

