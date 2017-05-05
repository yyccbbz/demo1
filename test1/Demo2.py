#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 2 . Python 数据类型
#
# 学习到现在，有人可能问了，Python 中就没有数组，没有集合吗？说实话我不知道怎么说，因为这种东西功能像数组，但我怎么用都感觉没有数组的味道。
# 有两种类似数组功能的数据类型，一种是列表，一种是元组，下面来逐一介绍。

# lanagues = ["Python", "Java", "PHP", "C#"]
# print lanagues[1]
# lanagues[1] = "Unity"
# print lanagues[1]
#
# print lanagues

# 上面介绍的是列表，可以随意修改列表中的值，下面将介绍元组，元组中的元素一旦指定，就不能在修改，这是两者的差别

# lanagues = ("Python", "Java", "PHP", "C#")
#
# print lanagues
#
# print lanagues[1]
# lanagues[1] = "Unity"
# print lanagues[1]

# 可见，元组的声明和列表就是符号的差别，列表是中括号，元组是小括号，这个时候如果运行会出现如下结果
#
# Java
# Traceback (most recent call last):
#   File "E:/PythonCode/TestOne/TestOne.py", line 5, in <module>
#     lanagues[1] = "Unity"
# TypeError: 'tuple' object does not support item assignment
# 打印出来 Java 之后，就出现了错误，错误信息的意思是元组类型的元素不支持修改，也就是只能读，不能写。


# 下面再来介绍中一种数据类型称之为集合，集合的主要功能有两点，一个功能是建立联系，一种功能是消除重复元素。

# a = set("aaabbbcccdddeee")
# b = set("bbccff")
#
# c = a & b
# d = a | b
# e = a - b
#
# print ("a = {0}".format(a))
# print ("b = {0}".format(b))
# print ("c = {0}".format(c))
# print ("d = {0}".format(d))
# print ("e = {0}".format(e))

# 看一下输出结果，就能对集合的功能有个大致的掌握
#
# set(['a', 'c', 'b', 'e', 'd'])
# set(['c', 'b', 'f'])
# set(['c', 'b'])
# set(['a', 'c', 'b', 'e', 'd', 'f'])
# set(['a', 'e', 'd'])
# 可见 c就是 a 交 b,d 就是 a 并 b，e 就是 a与b 的差，而且可以看到输出结果中重复元素就被自动消除了，只保留了一个。


# 下面再看看 Python 中的字典，其实字典的格式和 JSON 数据格式是一样的，为什么这么说呢？

person = {"name": "hwaphon", "sex": "man", "age": "18"}

person["tel"] = "1889533"

print person["tel"]
print person

