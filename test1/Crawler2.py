#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 在网页源代码中爬取图片链接并下载

# 这篇文章中只是网络爬虫的第一步，所以讲解的也比较浅，所以现在我们先来利用正则表达式实现一个手动的网络爬虫，什么是手动的呢？
# 就是我们自己把网页源代码复制下来，保存在一个 txt 文件中，然后利用正则表达式去过滤信息，然后去下载。
# http://mt.sohu.com/20150704/n416157015.shtml
# pip install requests
'''
print pic_url:
['http://n1.itc.cn/img8/wb/smccloud/fetch/2015/07/04/112732422680200576.JPG',
 'http://n1.itc.cn/img8/wb/smccloud/fetch/2015/07/04/112640070563900918.JPG',
 'http://n1.itc.cn/img8/wb/smccloud/fetch/2015/07/04/112547718465744154.JPG',
 'http://n1.itc.cn/img8/wb/smccloud/fetch/2015/07/04/112455366330382227.JPG',
 'http://n1.itc.cn/img8/wb/smccloud/fetch/2015/07/04/112363014254719641.JPG',
 'http://n1.itc.cn/img8/wb/smccloud/fetch/2015/07/04/112270662197888742.JPG',
 'http://n1.itc.cn/img8/wb/smccloud/fetch/2015/07/04/112178310031994750.JPG',
 'http://n1.itc.cn/img8/wb/smccloud/fetch/2015/07/04/112085957910403853.JPG']
 
 首先打开我们保存网络源代码的 txt文件，进行读取，关闭文件流，然后就是利用正则表达式提取图片链接，
 最后利用requests 中的 get() 方法进行图片下载，注意这个 requests 不是Python 中自带的，需要单独安装。
'''

import re
import requests

f = open('source.txt', 'r')
html = f.read()
f.close()

pattern = '<img src="(.*?)"'
pic_url = re.findall(pattern, html, re.S)
i = 0
for each in pic_url:
    print 'Downloading :' + each
    pic = requests.get(each)
    fp = open('picture\\' + str(i) + '.jpg', 'wb')
    fp.write(pic.content)
    fp.close()
    i = i + 1

