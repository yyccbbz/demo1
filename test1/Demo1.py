#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 1 . 数与字符串
# Python 中数有 5 中类型, 分别为 int（有符号整数型） ， long（长整型） ,  float（浮点型） ,  bool （布尔型） , complex （复数型）

# a = 10
# b = 3.14
# c = 10l
# d = True
# e = 5 + 2j
#
# print a
# print b
# print c
# print d
# print e

# 其中 complex 类型可能不常见，在其他编程语言中想要表示复数，都需要自定义，
# 比如在 Java 中，我们就需要定义一个类，然后声明两个实例变量，一个表示实部，一个表示虚部。

# Python 中字符串使用的引号可以是单引号，也可以是双引号，更可以是三引号，不得不承认，创造 Python 的人脑洞真大，下面来看看这三种引号的用法。

# a = 'Hello Python'
# b = "Hello Python"
# c = '''Hello Python'''
# d = """Hello Python"""
#
# print a
# print b
# print c
# print d

# 运行一下，发现都可以输出，但是这三种引号有什么特殊的用途？
# 首先，在单引号中可以再次使用双引号，在双引号中也可以使用单引号，以此满足特定的需要，什么意思，看看下面这个例子

# a = 'Python says "How are you?"'
# b = "I'm good"
#
# print a
# print b

# 打印出结果，如下
#
# Python says "How are you?"
# I'm good
# 怎么样？现在知道是干什么用的了吧？在其他编程语言中我们要做到相同的结果需要借助于转义字符。 好了，那么三个引号是干什么用的呢？

# a = '''Hello
# World
# I
# am
# Python'''
#
# print a

# 打印结果
#
# Hello
# World
# I
# am
# Python
# 可见，用了三个引号之后，我们就可以将字符串任意换行，而且输出时会保留我们输入的格式。

# 下面来看看转义字符的使用，以此引出对自然字符串的介绍，想要达到上述单引号双引号混合的结果，可以使用转义字符来实现，如下

# a = 'I\'m good'
#
# print a
# 上述字符串，如果没有转义字符，那就会报错，因为编译器会认为 a 的值为 I，而后面的字符串不知道是什么，还有很多利用转义字符实现的功能，比如换行 \n。
# 什么是自然字符串呢？就是对字符串中的内容不作处理，直接输出。怎么使用自然字符串呢？在字符串的引号前头加上 r。

# a = "Hello\nPython"
# b = r"Hello\nPython"
#
# print a
# print b

# 结果如下
#
# Hello
# Python
# Hello\nPython
# 好了，准备好，下面将介绍一个字符串逆天的打印功能。在其他语言中如果我们想要重复打印一个字符串，那么我们需要使用循环，然后指定循环次数，而在 Python 中呢？

# a = "Hello Python\n"
#
# print a * 5
# 就是这样，需要打印几次，就 * 几即可。

# 下面来看看如何获取一个字符串的子字符串，在 Java 中有一个方法叫做 substring() ，利用这个方法即可获取子字符串，那么在 Python 中呢？
# 首先我们来看看如何获取字符串中一个指定位置的字符->

a = "Hello Python"
b = a[1]

print a
print b

# 这样我们就可以获取 a 字符串中的第二个字符，因为序号是从 0 开始的，是不是感觉这就像一个数组一样？那么我们如何获取多个字符呢？
# 比如我想获取序号 1-5 的字符组成的字符串，利用这种方法即可

b = a[1:6]

print b

# 注意这里我们使用的是 1:6，还有这里的 1 如果我们不指定，默认是 0。