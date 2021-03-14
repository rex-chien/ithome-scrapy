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

# 搜尋標籤 "b"
print(soup.find_all('b'))
# [<b>爬蟲在手、資料我有</b>]

# 搜尋以 "b" 開頭的標籤
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
# body
# b

# 搜尋標籤 "a" 和 "b"
print(soup.find_all(["a", "b"]))
# [<b>爬蟲在手、資料我有</b>,
#  <a href="http://example.com/environment" class="page" id="link1">準備環境</a>、
#  <a href="http://example.com/csv" class="page" id="link2">CSV</a>、
#  <a href="http://example.com/json" class="page" id="link3">JSON</a>]

def has_class_but_no_id(tag):
    """ 判斷標籤是否定義 class 屬性且無定義 id 屬性
    """
    return tag.has_attr('class') and not tag.has_attr('id')

print(soup.find_all(has_class_but_no_id))
# [<p class="title"><b>爬蟲在手、資料我有</b></p>,
#  <p class="story">基礎知識</p>,
#  <p class="story">...</p>]
