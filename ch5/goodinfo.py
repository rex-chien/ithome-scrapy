import requests
from fake_useragent import UserAgent
from urllib.parse import urlencode
from bs4 import BeautifulSoup

url_root = 'https://goodinfo.tw/StockInfo/ShowK_Chart.asp'

payload = {
    'STOCK_ID': '0050',
    'CHT_CAT2': 'DATE',
    'STEP': 'DATA',
    'PERIOD': 365
}
qs = urlencode(payload)
url = f'{url_root}?{qs}'

ua = UserAgent()
headers = {
    'user-agent': ua.random,
    'referer': url
}

response = requests.post(url, headers=headers)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'lxml')
rows = soup.select('div#divPriceDetail > table > tr')
k_data = []
for row in rows:
    columns = row.select('td')

    k_data.append({
        'day': columns[0].get_text(strip=True),
        'open_price': float(columns[1].get_text(strip=True)),
        'high_price': float(columns[2].get_text(strip=True)),
        'low_price': float(columns[3].get_text(strip=True)),
        'close_price': float(columns[4].get_text(strip=True))
    })

