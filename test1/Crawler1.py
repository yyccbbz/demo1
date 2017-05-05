#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 正则表达式的使用

# 想要学习 Python 爬虫 ， 首先需要了解一下正则表达式的使用，下面我们就来看看如何使用。

# . 的使用
# 这个时候的点就相当于一个占位符，可以匹配任意一个字符，什么意思呢？看个例子就知道

import re

content = "helloworldhelloworld"
b = re.findall('w.', content)
print ("b1 = {0}".format(b))
# 注意了，我们首先导入了 re，这个时候大家猜一下输出结果是什么？因为 . 相当于一个占位符，所以理所当然的这个时候的输出结果是 wo 。

# * 的使用
# 跟上面的 . 不同，* 可以匹配前一个字符任意次数，看个例子

content = "helloworldhelloworld"
b = re.findall('w*', content)
print ("b2 = {0}".format(b))
# 这个时候的输出结果是 ['', '', '', '', '', 'w', '', '', '', '', '', '', '', '', '', 'w', '', '', '', '', '']，
# 可见是一个列表，长度和匹配的字符串一致，遇到要匹配的字符就打印出来。

# .* 的使用
# .* 是一种组合使用，它可以尽可能多的匹配内容，比如下面这个例子

content = "helloworldhelloworldworld"
b = re.findall('he.*ld', content)
print ("b3 = {0}".format(b))
# 它会输出 ['helloworldhelloworldworld']，它为什么不只打印一个 helloworld，为什么全部打印下来了？
# 这就是一种贪心算法，也就是说我要找到最长的那个符合条件的内容。

# .*? 的使用
# 与 上面相反，这个符号会找到尽可能短的符合条件的内容，然后放到一个列表中去，如下所示

content = 'xxhelloworldxxxxhelloworldxx'
b = re.findall('xx.*?xx', content)
print ("b4 = {0}".format(b))
# 输出的结果为 ['xxhelloworldxx', 'xxhelloworldxx']，
# 可见，有个 xx 在前面好烦，怎么才能去掉呢？很简单，加个括号即可，括号加在哪？

content = 'xxhelloworldxxxxhelloworldxx'
b = re.findall('xx(.*?)xx', content)
print ("b5 = {0}".format(b))
# 以上我们讨论的都是内容不包含换行符的情况，如果有了换行符结果又会发生什么变化呢？

content = '''xxhelloworld
xx'''
b = re.findall('xx(.*?)xx', content)
print ("b6 = {0}".format(b))
# 这个时候的输出结果为一个空列表，那怎么办啊？如果我们写网络爬虫的时候，网页源代码肯定不止是一行啊，
# 如果换一行我们就读不出来了，那就好尴尬了，当然有解决办法~

content = '''xxhelloworld
xx'''
b = re.findall('xx(.*?)xx', content, re.S)
print ("b7 = {0}".format(b))
# 这样就可以了，还有一个非常方便的提取数字的技巧，如下所示

content = '''xx123456
xx'''
b = re.findall('(\d+)', content, re.S)
print ("b8 = {0}".format(b))



# 在网页源代码中爬取图片链接并下载

# 这篇文章中只是网络爬虫的第一步，所以讲解的也比较浅，所以现在我们先来利用正则表达式实现一个手动的网络爬虫，什么是手动的呢？
# 就是我们自己把网页源代码复制下来，保存在一个 txt 文件中，然后利用正则表达式去过滤信息，然后去下载。
# http://mt.sohu.com/20150704/n416157015.shtml
'''
['http://n1.itc.cn/img8/wb/smccloud/fetch/2015/07/04/112732422680200576.JPG',
 'http://n1.itc.cn/img8/wb/smccloud/fetch/2015/07/04/112640070563900918.JPG',
 'http://n1.itc.cn/img8/wb/smccloud/fetch/2015/07/04/112547718465744154.JPG',
 'http://n1.itc.cn/img8/wb/smccloud/fetch/2015/07/04/112455366330382227.JPG',
 'http://n1.itc.cn/img8/wb/smccloud/fetch/2015/07/04/112363014254719641.JPG',
 'http://n1.itc.cn/img8/wb/smccloud/fetch/2015/07/04/112270662197888742.JPG',
 'http://n1.itc.cn/img8/wb/smccloud/fetch/2015/07/04/112178310031994750.JPG',
 'http://n1.itc.cn/img8/wb/smccloud/fetch/2015/07/04/112085957910403853.JPG']
'''






