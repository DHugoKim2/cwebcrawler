import selenium
from selenium.webdriver.common.by import By as by
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome("컴퓨터에서 크롬 위치 입력", options = options)
browser.get('https://fmkorea.com')

id, pw = input().split()

log_in = browser.find_element(by.NAME, 'user_id')
log_in.clear()
log_in.send_keys(id)

log_in_pw = browser.find_element(by.NAME, 'password')
log_in_pw.clear()
log_in_pw.send_keys(pw)

log_in_pw.send_keys(keys.ENTER)

address = str(input())
browser.get(address)
elements = browser.find_elements(by.CLASS_NAME, "voted_count")

for element in elements:
    element.click()