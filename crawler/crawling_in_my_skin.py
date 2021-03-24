from os import path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/home/victor/auxinas/experiment_crawler/chromedriver')

browser = driver.get('https://sindpd.org.br/sindpd/site/')

links = driver.find_elements_by_tag_name('a')

print (links)