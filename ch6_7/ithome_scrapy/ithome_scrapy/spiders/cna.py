import scrapy
from datetime import datetime

from ithome_scrapy import items


class CnaSpider(scrapy.Spider):
    name = 'cna'
    allowed_domains = ['www.cna.com.tw']
    api_url = 'https://www.cna.com.tw/cna2018api/api/WNewsList'
    data = {
        'action': '0',
        'category': 'aopl',
        'pageidx': 1,
        'pagesize': 50,
    }

    def start_requests(self):
        yield scrapy.http.JsonRequest(url=self.api_url, data=self.data, callback=self.parse)

    def parse(self, response):
        result = response.json()
        items = result['ResultData']['Items']

        for item in items:
            article_url = item['PageUrl']

            yield response.follow(article_url, callback=self.parse_content)

        if 'NextPageIdx' in result:
            self.data['pageidx'] = result['NextPageIdx']
            yield scrapy.http.JsonRequest(url=self.api_url, data=self.data, callback=self.parse)


    def parse_content(self, response):
        article = items.ArticleItem()

        article_content = response.css('article > div.centralContent')
        title = article_content.css('h1 ::text').get().strip()
        datetime_str = article_content.css('div.updatetime > span::text').get().strip()
        publish_time = datetime.strptime(datetime_str, '%Y/%m/%d %H:%M')

        content_list = article_content.css('div.paragraph p::text').getall()
        stripped_content_list = filter(lambda text: text, map(lambda elm: elm, content_list))
        content = ' '.join(stripped_content_list)

        article['url'] = response.url
        article['title'] = title
        article['publish_time'] = publish_time
        article['content'] = content

        yield article
