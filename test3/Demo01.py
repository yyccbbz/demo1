# -*- coding: UTF-8 -*-


# 练习1.第一个程序
print "Hello World!"
print "Hello Again"
print "I like typing this."
print "This is fun."
print 'Yay! Printing.'
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'

print "----------------------------------------------------------------------------------------------------------------"
# 练习2.注释和井号“#”
# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.

print "I could have code like this." # and the comment after is ignored

# You can also use a comment to "disable" or comment out a piece of code:
# print "This won't run."

print "This will run."
print "Hi # there."

print "----------------------------------------------------------------------------------------------------------------"
# 练习3.数字和数学计算
'''
+ plus 加号 
- minus 减号
/ slash 斜杠 除法
* asterisk 星号 乘法
% percent 百分号 模除
< less-than 小于号
> greater-than 大于号
<= less-than-equal 小于等于号
>= greater-than-equal 大于等于号
'''

print "I will now count my chickens:"

print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

print "4----------------------------------------------------------------------------------------------------------------"
# 练习4.变量和命名
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
# 字符串拼接
print "Hey %s there." % "you"

print "5----------------------------------------------------------------------------------------------------------------"
# 练习5.更多的变量和打印
my_name = 'Zed A. Shaw'
my_age = 35  # not a lie
my_height = 74  # inches
my_weight = 180  # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

# 格式化字符 %s,%d, %r显示的是变量“原始”的数据值

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

print round(1.7333)

print "6----------------------------------------------------------------------------------------------------------------"
# 练习6.字符串和文本
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

# 用%r显示的是变量“原始”的数据值，%r在打印的时候能够重现它代表的对象，
# 但其他的符号用来给用户显示变量值。
text = "I am %d years old." % 22
print "I said: %s." % text
print "I said: %r." % text


print "7----------------------------------------------------------------------------------------------------------------"
# 练习7.更多的打印（输出）
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10  # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

print "8----------------------------------------------------------------------------------------------------------------"
# 练习8.打印, 打印
formatter = "%r %r %r %r"
# formatter = "%s %s %s %s"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)


print "9----------------------------------------------------------------------------------------------------------------"
# 练习9.打印, 打印, 打印
# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""




print "10----------------------------"
# 练习10.那是什么?
a = "I am 6'2\" tall."  # 将字符串中的双引号转义
b = 'I am 6\'2" tall.'  # 将字符串中的单引号转义

print a
print b

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# 转义字符
# while True:
#     for i in ["/","-","|","\\","|"]:
#         print "%s\r" % i,

print "11----------------------------"


print "12----------------------------"


print "13----------------------------"


print "14----------------------------"


print "15----------------------------"


print "16----------------------------"


print "17----------------------------"


print "18----------------------------"


print "19----------------------------"


print "20----------------------------"


print "21----------------------------"


print "22----------------------------"
















