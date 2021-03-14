import scrapy
from datetime import datetime
import re

from ithome_scrapy import items

class IthomeSpider(scrapy.Spider):
    name = 'ithome'
    allowed_domains = ['ithome.com.tw']
    start_urls = ['https://ithelp.ithome.com.tw/articles?tab=tech']

    def parse(self, response):
        # 先找到文章區塊
        article_tags = response.css('div.qa-list')

        # 有文章才要繼續
        if len(article_tags) > 0:
            for article_tag in article_tags:
                # 再由每個區塊去找文章連結
                title_tag = article_tag.css('a.qa-list__title-link')
                article_url = title_tag.css('::attr(href)').get().strip()

                yield response.follow(article_url, callback=self.parse_article)

        next_page_url = response.css('a:contains("下一頁")::attr(href)').get()
        yield response.follow(next_page_url, callback=self.parse)

    def parse_article(self, response):
        leftside = response.css('div.leftside')
        original_post = leftside.css('div.qa-panel')

        article_header = original_post.css('div.qa-header')
        article_info = article_header.css('div.ir-article-info__content, div.qa-header__info')

        # 標題
        title = article_header.css('h2.qa-header__title::text').get().strip()

        # 作者
        author = article_info.css('a.ir-article-info__name, a.qa-header__info-person').css('::text').get().strip()

        # 發文時間
        published_time_str = article_info.css('a.ir-article-info__time, a.qa-header__info-time').css(
            '::text').get().strip()
        published_time = datetime.strptime(published_time_str, '%Y-%m-%d %H:%M:%S')

        # 文章標籤
        tag_group = article_header.css('div.qa-header__tagGroup')
        tag_elements = tag_group.css('a.tag')
        tags = [tag_element.css('::text').get().strip() for tag_element in tag_elements]

        # 內文
        content = ' '.join(original_post.css('div.markdown__style').css('::text').getall())

        # 瀏覽數
        view_count_str = article_info.css('.ir-article-info__view, .qa-header__info-view').css('::text').get().strip()
        view_count = int(re.search('(\d+).*', view_count_str).group(1))

        article = items.IthomeArticleItem()
        article['url'] = response.url
        article['title'] = title
        article['author'] = author
        article['publish_time'] = published_time
        article['tags'] = ''.join(tags)
        article['content'] = content
        article['view_count'] = view_count

        yield article

        if '_id' in article:
            '''
            上一行執行後資料已更新到資料庫中
            因為是同一個物件參照
            可以取得識別值
            '''
            article_id = article['_id']
            '''
            因為 iTHome 原文與回文都是在同一個畫面中
            剖析回文時使用原本的 response 即可
            否則這邊需要再回傳 Request 物件
            yield scrapy.Request(url, callback=self.parse_reply)
            '''
            yield from self.parse_reply(response, article_id)

    def parse_reply(self, response, article_id):
        leftside = response.css('div.leftside')
        replies = leftside.css('div.response')

        for reply in replies:
            panel = reply.css('div.qa-panel__content')
            header = panel.css('div.response-header__info')

            reply_item = items.IthomeReplyItem()
            reply_item['article_id'] = article_id

            # 回應 ID
            reply_item['_id'] = int(reply.css('a::attr(name)').get().replace('response-', ''))

            # 回應作者
            reply_item['author'] = header.css('a.response-header__person').css('::text').get()

            # 回應時間
            time_str = header.css('a.ans-header__time').css('::text').get().strip()
            reply_item['publish_time'] = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')

            # 回應內容
            reply_item['content'] = ' '.join(panel.css('div.markdown__style').css('::text').getall())

            yield reply_item