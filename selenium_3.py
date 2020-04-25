import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import etree
import time
#from selenium.webdriver.common.by import by

name = '13550304571'
passwd = '123456fqp'
driver = webdriver.Chrome()
driver.get('https://auth.dxy.cn/accounts/login')
time.sleep(5)
current_window_1 = driver.current_window_handle
print(current_window_1)

button = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/a[2]/text()')
button.click()
dxname = driver.find_element_by_class_name('username')
dxname.send_keys(name)
dxpassword = driver.find_element_by_class_name('password')
dxpassword.send_keys(passwd)
dxsubmit = driver.find_element_by_tag_name('submit')
time.sleep(15)
submit.click()
time.sleep(15)
print(driver.page_source)
driver.quit()
