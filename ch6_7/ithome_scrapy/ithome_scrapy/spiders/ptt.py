import scrapy

from ithome_scrapy import items

class PttSpider(scrapy.Spider):
    name = 'ptt'
    allowed_domains = ['ptt.cc']
    # start_urls = ['https://www.ptt.cc/bbs/Gossiping/index.html']

    def start_requests(self):
        yield scrapy.Request(
            'https://www.ptt.cc/bbs/Gossiping/index.html',
            cookies={'over18': '1'},
            callback=self.parse
        )

    def parse(self, response):
        # if response.css('div.over18-notice'):
        #     yield scrapy.FormRequest.from_response(response,
        #                                            formdata={'yes': 'yes'},
        #                                            callback=self.parse,
        #                                            dont_filter=True)
        # else:
        article_tags = response.css('div.r-ent')[::-1]

        if article_tags:
            for item in article_tags:
                link_tag = item.css('div.title a')

                if link_tag:
                    # ...取得文章連結
                    article_url = response.urljoin(link_tag.css('::attr(href)').get())
                    title = link_tag.css('::text').get().strip()
                    article = items.ArticleItem()
                    article['url'] = article_url
                    article['title'] = title
                    yield article

                    # yield response.follow(article_url, callback=self.parse_article)

            prev_page_url = response.css('a:contains("‹ 上頁")::attr(href)').get()
            yield response.follow(url=prev_page_url, callback=self.parse)
