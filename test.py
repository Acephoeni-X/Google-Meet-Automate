from selenium import webdriver
import time



if __name__ == "__main__":
  browser = webdriver.Chrome()
  browser.get('https://stackoverflow.com/users/login')
  time.sleep(10)
