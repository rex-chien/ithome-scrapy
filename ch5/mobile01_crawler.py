from urllib.parse import urljoin
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'User-Agent': ua.random}

url = 'https://www.mobile01.com/forumtopic.php?c=17'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
last_page = int(soup.select('a.c-pagination')[-1].get_text(strip=True))

for page in range(1, last_page + 1):
    items = soup.select('div.l-listTable__tbody > div.l-listTable__tr')
    for item in items:
        link_tag = item.select_one('div.c-listTableTd__title > a')
        article_url = urljoin('https://www.mobile01.com/', link_tag['href'])
        article_response = requests.get(article_url, headers=headers)
        article_soup = BeautifulSoup(article_response.text, 'lxml')
        article_last_page = int(article_soup.select('a.c-pagination')[-1].get_text(strip=True))

        for article_page in range(1, last_page + 1):
            article_pages = article_soup.select('div.l-articlePage')
            main_article = article_pages[0]

            title = main_article.select_one('div.l-heading__title > h1').get_text(strip=True)
            toolbar = main_article.select('ul.l-toolBar')[0]
            datetime_str = toolbar.select('span')[0].get_text(strip=True)
            published_date = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
            author = main_article.select_one('div.c-authorInfo__id > a').get_text(strip=True)

            content = main_article.select_one('article').get_text(strip=True)

            article_url = article_url

    url = f'https://www.mobile01.com/forumtopic.php?c=17&p={page}'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
