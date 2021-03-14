import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re


def crawl_list():
    """爬取文章列表頁
    """
    # 抓取 1~10 頁
    for page in range(1, 11):
        html_doc = requests.get(f'https://ithelp.ithome.com.tw/articles?tab=tech&page={page}').text
        soup = BeautifulSoup(html_doc, 'lxml')

        # 先找到文章區塊
        article_tags = soup.find_all('div', class_='qa-list')

        # 沒有文章
        if len(article_tags) == 0:
            # 跳出換頁迴圈或離開程式
            print('沒有文章了！')
            break

        articles = []

        for article_tag in article_tags:
            # 再由每個區塊去找文章連結
            title_tag = article_tag.find('a', class_='qa-list__title-link')
            article_url = title_tag['href']

            articles.append(crawl_content(article_url))


def crawl_content(url):
    """爬取文章內容
    :param url: 文章連結
    """
    html_doc = requests.get(url).text
    soup = BeautifulSoup(html_doc, 'lxml')

    leftside = soup.find('div', class_='leftside')
    original_post = leftside.find('div', class_='qa-panel')

    article_header = original_post.find('div', class_='qa-header')
    article_info = article_header.find('div', class_=['ir-article-info__content', 'qa-header__info'])

    # 標題
    title = article_header.find('h2', class_='qa-header__title').get_text(strip=True)

    # 作者
    author = article_info.find('a', class_=['ir-article-info__name', 'qa-header__info-person']).get_text(strip=True)

    # 發文時間
    published_time_str = article_header.find('a', class_=['ir-article-info__time', 'qa-header__info-time']).get_text(strip=True)
    published_time = datetime.strptime(published_time_str, '%Y-%m-%d %H:%M:%S')

    # 文章標籤
    tag_group = article_header.find('div', class_='qa-header__tagGroup')
    tags_element = tag_group.find_all('a', class_='tag')
    tags = [tag_element.get_text(strip=True) for tag_element in tags_element]

    # 內文
    content = original_post.find('div', class_='markdown__style').get_text(strip=True)

    # 瀏覽數
    view_count_str = article_info.find(['div', 'span'], class_=['ir-article-info__view', 'qa-header__info-view']).get_text(strip=True)
    view_count = int(re.search(r'(\d+).*', view_count_str).group(1))

    article = {
        'url': url,
        'title': title,
        'author': author,
        'publish_time': published_time,
        'tags': tags,
        'content': content,
        'view_count': view_count,
        'responses': crawl_response(soup)
    }

    return article


def crawl_response(soup):
    """爬取文章回應

    :param soup: 因為跟原文跟回應在同一個畫面，這邊偷懶直接用文章的 soup 物件
    """
    leftside = soup.find('div', class_='leftside')
    responses = leftside.find_all('div', class_='response')

    results = []

    for response in responses:
        panel = response.find('div', class_='qa-panel__content')
        header = panel.find('div', class_='response-header__info')

        result = {}

        # 回文作者
        result['author'] = header.find('a', class_='response-header__person').get_text(strip=True)

        # 回應時間
        time_str = header.find('a', class_='ans-header__time').get_text(strip=True)
        result['publish_time'] = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')

        # 回文內容
        result['content'] = panel.find('div', class_='markdown__style').get_text(strip=True)

        results.append(result)

    return results


if __name__ == '__main__':
    crawl_list()
