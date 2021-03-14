from requests_html import HTMLSession
from bs4 import BeautifulSoup

session = HTMLSession()
r = session.get('https://pythonclock.org/')

r.html.render()
soup = BeautifulSoup(r.html.html, 'lxml')

print(soup.find('div', class_='python-27-clock'))
print(r.html.find('div.python-27-clock'))
