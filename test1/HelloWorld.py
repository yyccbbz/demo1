#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: HelloWorld.py

###############coding=utf-8#################

# if True:
#     print "Answer"
#     print "True"
# else:
#     print "Answer"
#     # 没有严格缩进，在执行时会报错
#     print "False"
#
# days = ['Monday', 'Tuesday', 'Wednesday',
#         'Thursday', 'Friday']
#
# print days

# 3 . 定义变量
# Python 语言声明变量也十分方便，方便到以前不敢想

# a = 10  # 声明一个 int 型变量
# b = 'h'  # 声明一个 char 变量
# c = "Hello Python"  # 声明一个 String 变量
#
# print a,b,c

# 4 . 判断语句
# 判断语句就有需要注意的地方了，要在有 if ，elif 或者 else 的行尾加上‘：’符号，注意是冒号，不是分号

# score = 100
#
# if score >= 90:
#     print ("很好")
# elif score >= 60:
#     print ("及格")
# else:
#     print ("差劲")
#
# print "-------------------------------------------------"

# 5 . 循环
# 使用循环仍然需要注意在 for 的末尾加上 冒号

# for i in range(0, 100):
#     print (i)
# 这样就可以实现打印 0-99，所以也可以看出， range里面的两个数的执行规则是 start<= i < end，看到这里有人想了，广打印 i 多没劲啊，我还要加字符串，于是写成

# for i in  range(0,100):
#     print ("Item " + i)
# 结果非常尴尬，出现了错误，在 Python 是不支持这种写法的，如果要在 i 前面或者后面加字符串，我们可以这么写

# for i in range(0, 100):
#     print ("Item {0}".format(i))
#
# print "-------------------------------------------------"
#
# for i in range(0, 100):
#     print ("Item {0} {1}".format(i, "Hi"))
# 感觉有点像 C 语言，输出时以 %d,%f 等格式指定，只不过这里直接指定序号而已。

# 6 . 定义函数

# def sayHello():
#     print ("Hello Python")
#
# sayHello()

# 看代码看到现在也应该看出来了，打了冒号之后，底下连续的缩进的代码行都属于同一个代码块，是一个整体。
# 上面定义的是一个不带参数的自定义函数，那么带参数的函数怎么定义呢？

# def sayHello(name):
#     print ("Hello {0}".format(name))
#
#
# sayHello("Python")
#
#
# def max(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
#
# a = max(1, 2)
# print (a)


# 7 . 面向对象
# 自从开往对象村，就再也不想回去了，Python 如果不支持对象，那咱就别学了，哈哈，下面看看怎么声明一个类

# class Person:
#     def sayHello(self):
#         print ("Hello Python!!!")
#
#
# p = Person()
# p.sayHello()

# 类是有了，方法也有了，但是构造函数呢？
class Person:
    def __init__(self, name):
        self._name = name

    def sayHello(self):
        print ("Hello {0}".format(self._name))


p = Person("Python")
p.sayHello()

# 既然是面向对象，那继承总的有吧？怎么继承呢？

class Student(Person):
    def __init__(self, name):
        Person.__init__(self, name)

    def sayHi(self):
        print ("Hi {0}".format(self._name))


s = Student("Python")
s.sayHi();
s.sayHello()


# 8 . 引入 Python文件
# 引入 Python 文件？什么意思？意思就是我新建了一个工具类，我怎么在别处引用它？比如我写了一个 名为 Helper.py 的工具类，里面的类如下所示

class HelpUtil:
    def max(self, a, b):
        if a > b:
            return a
        else:
            return b

# 我又建了一个 Test.py ，我想使用 Helper.py 中的 max 函数，怎么办？

# import Helper
#
# h = Helper.HelpUtil()
# a = h.max(1, 2)
# print (a)
# 除了这一种方式，我们还可以用另一种方法
#
# from Helper import HelpUtil
#
# h = HelpUtil()
# a = h.max(1,2)
# print (a)
# 这种方式直接指定导入了这个类，这样的话获取新的实例就方便些。好了，今天就先介绍些基础，后续还会继续更新关于Python 的文章。