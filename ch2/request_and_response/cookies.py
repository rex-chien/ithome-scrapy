import requests

url = 'https://httpbin.org/cookies'
cookies = {
    'ithome': 'scrapy'
}

r = requests.get(url, cookies=cookies)
print(r.text)
