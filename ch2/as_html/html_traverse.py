from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
    <title>爬蟲在手、資料我有</title>
</head>

<body>
    <p class="title"><b>爬蟲在手、資料我有</b></p>
    <p class="chapter">基礎知識
        <a href="http://example.com/environment" class="page" id="link1">準備環境</a>、
        <a href="http://example.com/csv" class="page" id="link2">CSV</a>、
        <a href="http://example.com/json" class="page" id="link3">JSON</a>
    </p>
    <p class="chapter">...</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'lxml')

print(soup.prettify())

# 取得 head 標籤
print(soup.head)
# <head><title>爬蟲在手、資料我有</title></head>

# 取得 head 下的 title 標籤
print(soup.head.title)
# <title>爬蟲在手、資料我有</title>

# 取得「第一個」a 標籤
print(soup.a)
# <a href="http://example.com/environment" class="page" id="link1">準備環境</a>

# 取得直屬 body 的所有下層標籤，回傳 list 類型
print(soup.body.contents)

# 取得第一個a 標籤的上層標籤
print(soup.a.parent)

# 取得與第一個 a 標籤同層級的下一個「元素」
print(soup.a.next_sibling)
# '、\n'
