#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: HelloWorld2.py

# 8 . 引入 Python文件
# 引入 Python 文件？什么意思？意思就是我新建了一个工具类，我怎么在别处引用它？比如我写了一个 名为 Helper.py 的工具类，里面的类如下所示

# class HelpUtil:
#     def max(self, a, b):
#         if a > b:
#             return a
#         else:
#             return b

# 我又建了一个 Test.py ，我想使用 Helper.py 中的 max 函数，怎么办？

# import HelloWorld
#
# h = HelloWorld.HelpUtil()
# a = h.max(1, 2)
# print (a)

# 除了这一种方式，我们还可以用另一种方法

from HelloWorld import HelpUtil

h = HelpUtil()
a = h.max(1, 2)
print (a)
# 这种方式直接指定导入了这个类，这样的话获取新的实例就方便些。好了，今天就先介绍些基础，后续还会继续更新关于Python 的文章。