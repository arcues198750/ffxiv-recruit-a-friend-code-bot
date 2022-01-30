import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait       
from selenium.webdriver.common.by import By       
from selenium.webdriver.support import expected_conditions as EC

sqexid = 'username'
sqexpw = 'password'

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://secure.square-enix.com/account/app/svc/mogstation')
time.sleep(1)

browser.find_element_by_id('sqexid').send_keys(sqexid)
browser.find_element_by_id('password').send_keys(sqexpw)
browser.find_element_by_id('login-button').click()
time.sleep(1)

test = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/form/div/div/div[13]/a[2]/div[1]/img')
browser.execute_script("arguments[0].click();", test)
time.sleep(600)
