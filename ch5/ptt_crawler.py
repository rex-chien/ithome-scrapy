from urllib.parse import urljoin
from datetime import datetime

import requests
from bs4 import BeautifulSoup

url_prefix = 'https://www.ptt.cc/'
list_url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
headers = {'cookie': 'over18=1;'}

while True:
    response = requests.get(list_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    items = soup.select('div.r-ent')
    for item in items:
        link_tag = item.select_one('div.title > a')
        if link_tag:
            article_url = urljoin(url_prefix, link_tag['href'])
            title = link_tag.get_text(strip=True)

            response = requests.get(article_url, headers=headers)
            article_soup = BeautifulSoup(response.text, 'lxml')
            main_content = article_soup.select_one('#main-content')
            meta_lines = main_content.select('div.article-metaline')
            author = meta_lines[0].select_one('span.article-meta-value').get_text(strip=True)
            datetime_str = meta_lines[2].select_one('span.article-meta-value').get_text(strip=True)
            published_date = datetime.strptime(datetime_str, '%a %b %d %H:%M:%S %Y')

            content_list = main_content.find_all(text=True, recursive=False)
            stripped_content_list = filter(lambda text: text, map(lambda text: text.strip(), content_list))
            content = ' '.join(stripped_content_list)

    paging_btns = soup.select('div.btn-group-paging > a.btn.wide')
    list_url = urljoin(url_prefix, paging_btns[1]['href'])
