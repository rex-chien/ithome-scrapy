from pymongo import MongoClient
from datetime import datetime

host = 'localhost'
dbname = 'ithome'

client = MongoClient(host, 27017)
print('資料庫連線成功！')

db = client[dbname]
article_collection = db.article

article = {
    'title': '【Day 0】前言',
    'url': 'https://ithelp.ithome.com.tw/articles/10215484',
    'author': 'Rex Chien',
    'publish_time': datetime(2019, 9, 15, 15, 50, 0),
    'tags': '11th鐵人賽,python,crawler,webscraping,scrapy',
    'content': '從簡單的商品到價提醒，到複雜的輿情警示、圖形辨識，「資料來源」都是基礎中的基礎。但網路上的資料龐大而且更新很快，總不可能都靠人工來蒐集資料。',
    'view_count': 129
}
article_id = article_collection.insert_one(article).inserted_id

print(f'資料新增成功！ID: {article_id}')

client.close()