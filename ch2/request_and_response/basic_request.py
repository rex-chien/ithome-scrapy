import requests

response = requests.get('https://ithelp.ithome.com.tw/')

# 回應狀態
print(response.status_code)
# 200

# 回應標頭
print(response.headers['content-type'])
# text/html; charset=UTF-8

# 回應的內容，是 bytes 類型
print(response.content)

# 回應的內容，是 unicode 字元，以 response.encoding 解碼
print(response.text)
