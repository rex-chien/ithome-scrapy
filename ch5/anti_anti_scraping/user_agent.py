import requests
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'User-Agent': ua.random}
requests.get('https://ithelp.ithome.com.tw/', headers=headers)
