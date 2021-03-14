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

# 找出 body 下的 a 標籤
print(soup.select('body a'))
# [<a href="http://example.com/environment" class="page" id="link1">準備環境</a>
#  <a href="http://example.com/csv" class="page" id="link2">CSV</a>
#  <a href="http://example.com/json" class="page" id="link3">JSON</a>]

# 找出 class 包含 page 的標籤
print(soup.select('.page'))
# [<a href="http://example.com/environment" class="page" id="link1">準備環境</a>
#  <a href="http://example.com/csv" class="page" id="link2">CSV</a>
#  <a href="http://example.com/json" class="page" id="link3">JSON</a>]

# 找出 id 是 link2 的標籤
print(soup.select('#link2'))
# [<a href="http://example.com/csv" class="page" id="link2">CSV</a>]

# 找出「第一個」class 包含 page 的標籤
print(soup.select_one('.page'))
# <a href="http://example.com/environment" class="page" id="link1">準備環境</a>
