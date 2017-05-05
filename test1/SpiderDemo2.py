# coding=utf-8

from lxml import etree

f = open('myHtml.html', 'r')
html = f.read()
f.close()

selector = etree.HTML(html)

# 提取 li 中的有效信息123
content = selector.xpath('//ul[@id="useful"]/li/text()')
for each in content:
    print(each)

# 提取 a 中的属性
link = selector.xpath('//a/@href')
for each in link:
    print(each)

title = selector.xpath('//a/@title')
for each in title:
    print(each)
