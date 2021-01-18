from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import schedule
import time

def automate(driver, link):
  driver.get(link)
  #driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div/span/span/div/div/svg').click()
  # wait = WebDriverWait(driver, 20)
  # wait.until(driver.get(link))
  # element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
  # element.send_keys("rishi.d.goku")
  driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys("rishi.d.goku")
  driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()

def schedule_time_table(browser):
  schedule.every().monday.at("13:25").do(automate, browser, 'https://accounts.google.com/ServiceLogin/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F&followup=https%3A%2F%2Fclassroom.google.com%2F&emr=1&flowName=GlifWebSignIn&flowEntry=AddSession')

  while True:
    schedule.run_pending()
    time.sleep(10)

if __name__ == "__main__":
  browser = webdriver.Chrome('/Users/acephoenix02/Google Drive/Documents/Python/Online-Class-Automation/chromedriver')
  schedule_time_table(browser)
  automate(browser)
  time.sleep(10)
