import requests
from bs4 import BeautifulSoup
from datetime import datetime

list_url = 'https://www.cna.com.tw/cna2018api/api/WNewsList'
data = {
    'action': '0',
    'category': 'aopl',
    'pageidx': 1,
    'pagesize': 50,
}

while True:
    list_response = requests.post(list_url, json=data)
    result = list_response.json()

    for item in result['ResultData']['Items']:
        article_url = item['PageUrl']

        article_response = requests.get(article_url)
        article_soup = BeautifulSoup(article_response.text, 'lxml')
        article_content = article_soup.select_one('article > div.centralContent')
        title = article_content.select_one('h1').get_text(strip=True)
        datetime_str = article_content.select_one('div.updatetime > span').get_text(strip=True)
        published_date = datetime.strptime(datetime_str, '%Y/%m/%d %H:%M')

        content_list = article_content.select_one('div.paragraph').select('p')
        stripped_content_list = filter(lambda text: text, map(lambda elm: elm.get_text(strip=True), content_list))
        content = ' '.join(stripped_content_list)

    next_page_idx = result['ResultData']['NextPageIdx']
    if not next_page_idx:
        break
    data['pageidx'] = next_page_idx
