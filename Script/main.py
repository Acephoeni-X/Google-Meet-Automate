import json
import requests
import   schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import requests
from datetime import datetime

TOKEN = "1532806948:AAHrR1O49Ow4J06-nVBqNo9I8XtFHmHLXGI"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    print(last_update)
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def start(link, chat):
    opt = Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    opt.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1,
        "detach": True
    })
    driver = webdriver.Chrome(options=opt,
                              executable_path="/Python_exe/chromedriver.exe")
    # driver = webdriver.Chrome()
    driver.get("https://google.com")
    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gb_70"]')))
    element.click()
    element = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="identifierId"]')))
    element.send_keys('rs1965@srmist.edu.in')
    element = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="identifierNext"]/div/button/div[2]')))
    element.click()
    
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
    element.send_keys('Firefist@ace2002')
    driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
    time.sleep(5)
    driver.get(link)
    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div')))
    element.click()
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div')))
    element.click()
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span')))
    element.click()
    send_message("class 1 started", chat)
    while True:
        text, chat = get_last_chat_id_and_text(get_updates())
        if(text == "/1stop"):
            exitprogram(driver)


def exitprogram(driver):
    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div')))
    element.click()
    send_message("class ended", text)
    main(text, chat)

def main(text, chat):
    while True:
        text, chat = get_last_chat_id_and_text(get_updates())
        if(text == "/1"):
            start("https://meet.google.com/lookup/ef4rgsip3e", chat)
        if(text =="/2"):
            start("https://meet.google.com/lookup/ceg7iq3out", chat)
        if(text == "/3"):
            start("https://meet.google.com/lookup/e6obb4y2fu", chat)
        if(text =="/4"):
            start("https://meet.google.com/lookup/dxynmk724s", chat)
        if(text == "/5"):
            start("https://meet.google.com/lookup/dbmj5o6tsn", chat)
        if(text =="/6"):
            start("https://meet.google.com/lookup/gkmtyn7lwr", chat)



text, chat = get_last_chat_id_and_text(get_updates())


