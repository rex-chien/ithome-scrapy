from lxml import etree

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

# 載入 HTML 原始資料
html = etree.HTML(html_doc)

print(html.xpath('/html'))
# [<Element html at 0x25ff3c8>]

print(html.xpath('/html/body/a'))
# []

print(html.xpath('//a'))
# [<Element html at 0x24e8788>, <Element html at 0x24e87b0>, <Element html at 0x26045a8>]

print(html.xpath('/html/body//a'))
# [<Element html at 0x24e8760>, <Element html at 0x26045a8>, <Element html at 0x2604a08>]

print(html.xpath('//a/@href'))
# ['http://example.com/environment', 'http://example.com/csv', 'http://example.com/json']
