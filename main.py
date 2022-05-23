from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://google.com')
driver.find_element_by_name("q").send_keys("UNASP")
driver.find_element_by_name("btnK").submit()
driver.find_element_by_css_selector('div.yuRUbf > a').click()
driver.find_element_by_css_selector('a.cc-ALLOW').click()
driver.find_element_by_css_selector('a#slider-135-slide-284-layer-28').click()
driver.find_element_by_xpath('//*[@id="listaDeCursosAncora"]/div/div/div[2]/a[1]').click()
driver.find_element_by_css_selector('body > div.una-page > div.una-summary.full-width > div.container > div > div:nth-child(2) > div > div > a:nth-child(3)').click()
time.sleep(200)