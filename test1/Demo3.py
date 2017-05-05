#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 3 . Python 对象的序列化
#
# 学习过 Java 的人都知道，如果我们想要保存一个对象的话，那么该对象必须是序列化的，也就是类需要实现  Serialization 接口。
# 那么在 Python 中我们如何序列化一个对象呢？又如何反序列化呢？
#
# 首先导入要使用的工具包

import pickle

# lista = ["Java", "Python"]
# listb = pickle.dumps(lista)
#
# print lista
# print listb

# 这个时候的 listb 就是lista 序列化之后的结果，下面来看看运行结果
# (lp0
# S'Java'
# p1
# aS'Python'
# p2
# a.

# 下面来看看如何反序列化

# listc = pickle.loads(listb)
# print listc

# 结果为 ['Java', 'Python']

# 序列化之后如何保存在文件当中呢？

lista = ["Java", "Python"]
f = file('1.pk1', 'wb')
print f
pickle.dump(lista, f, True)
f.close()

# 从文件中读取并且反序列化

f2 = file('1.pk1', 'rb')
print f2
listb = pickle.load(f2)
print listb
f2.close()


# 4 . 注释
#
# 注意，Python 语言的注释和其他语言有所不同，以往我们都是使用 // 或者 /* */ ，而在 Python 我们使用 # ，如下所示
#
# # coding=utf-8
#
#
# 这是一句注释
print "Hello Python"
