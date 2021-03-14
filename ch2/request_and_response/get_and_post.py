import requests

payload = {
    'search': 'python',
    'tab': 'question'
}
response = requests.get('https://ithelp.ithome.com.tw/search', params=payload)
print(response.url)

import pprint

payload = {
    'name': 'Rex',
    'topic': 'python'
}
response = requests.post('https://httpbin.org/post', data=payload)
pprint.pprint(response.json())
