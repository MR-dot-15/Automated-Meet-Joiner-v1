"""
    after being called by main.py 
    signs in, opens G-meet, turns off camera, mic
    and just joins/ waits while asking for permission 
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def join_meet(emailID, password, meet_link, driver):
    # logs in
    driver.get(
        'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')
    mail, pwd = emailID, password
    driver.find_element_by_id('identifierId').send_keys(mail)
    driver.find_element_by_id('identifierNext').click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath(
            '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(pwd)
    driver.implicitly_wait(10)
    driver.find_element_by_id("passwordNext").click()

    # reaches bulbul
    driver.get('https://google.com/')
    driver.implicitly_wait(100)

    # initiates an action chain
    action = ActionChains(driver)
    # reaches google meet
    driver.get(meet_link)
    action.key_down(Keys.CONTROL).send_keys("d").send_keys("e").key_up(Keys.CONTROL).perform()
    button = driver.find_element_by_xpath('//div[@role="button"]//span[contains(text(), "Join now")]')
    # waits until the 'button' is available 
    while True:
        try:
            button.click()
            break
        except:
            time.sleep(5)