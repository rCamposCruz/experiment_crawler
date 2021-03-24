from os import path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DOMAIN = 'sindpd.org.br'
FIRST_PAGE = 'https://sindpd.org.br/sindpd/site/'
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

BROWSER = webdriver.Chrome(chrome_options=chrome_options, executable_path='/home/victor/auxinas/experiment_crawler/chromedriver')
ALL_LINKS = []
CRAWLED = []

def isInDomain(link):
    print(link)
    try:
        return DOMAIN in link
    except:
        return

def isJspPage(link):
    return '.jsp' in link.lower()

def isDesiredDocument(link):
    return not isJspPage(link) and isInDomain(link)

def shouldCrawl(link):
    return isInDomain(link) and isJspPage(link)

def crawl(link):
    BROWSER.get(link)
    links = [link.get_attribute('href') for link in BROWSER.find_elements_by_tag_name('a')]
    ALL_LINKS.extend(links)
    linksToCrawl = [link for link in links if shouldCrawl(link)]
    for link in [link for link in linksToCrawl if link not in CRAWLED]:
        CRAWLED.append(link)
        crawl(link)

crawl(FIRST_PAGE)
print(ALL_LINKS)
