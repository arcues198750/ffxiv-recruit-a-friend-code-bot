from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

sqexid = "username"
sqexpw = 'password'

#Let's initiate the browser
browser = webdriver.Chrome(ChromeDriverManager().install())

#Let's open the actual browser up though
browser.get('https://secure.square-enix.com/account/app/svc/mogstation')

browser.find_element_by_id('sqexid').send_keys(sqexid)
browser.find_element_by_id('password').send_keys(sqexpw)

browser.find_element_by_id('login-button').click()

browser.find_element_by_link_text('Issue Recruitment Code').click();