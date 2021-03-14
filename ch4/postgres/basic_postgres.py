import psycopg2
from datetime import datetime

host = 'localhost'
user = 'postgres'
dbname = '<your_database>'
password = '<server_admin_password>'

conn_string = f'host={host} user={user} dbname={dbname} password={password}'
conn = psycopg2.connect(conn_string)
print('資料庫連線成功！')

cursor = conn.cursor()

article = {
    'title': '【Day 0】前言',
    'url': 'https://ithelp.ithome.com.tw/articles/10215484',
    'author': 'Rex Chien',
    'publish_time': datetime(2019, 9, 15, 15, 50, 0),
    'tags': '11th鐵人賽,python,crawler,webscraping,scrapy',
    'content': '從簡單的商品到價提醒，到複雜的輿情警示、圖形辨識，「資料來源」都是基礎中的基礎。但網路上的資料龐大而且更新很快，總不可能都靠人工來蒐集資料。'
}
cursor.execute('''
    INSERT INTO public.ithome_article(title, url, author, publish_time, tags, content)
    VALUES (%(title)s,%(url)s,%(author)s,%(publish_time)s,%(tags)s,%(content)s);
    ''',
    article)

print('資料新增成功！')

conn.commit()
cursor.close()
conn.close()
