from selenium import webdriver
from bs4 import BeautifulSoup

# 指定剛剛下載的 webdriver 路徑
driver = webdriver.Chrome('./chromedriver.exe')
# 用瀏覽器連到 pythonclock
driver.get('https://pythonclock.org/')

html_doc = driver.page_source
driver.close()
soup = BeautifulSoup(html_doc, 'lxml')

print(soup.find('div', class_='python-27-clock'))
