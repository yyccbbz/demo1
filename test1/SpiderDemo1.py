# coding=utf-8

import re
import requests
import sys

reload(sys)
sys.setdefaultencoding("utf8")


class spider():
    def __init__(self):
        print "开始爬取内容。。。"

    def changePage(self, url, total_page):
        nowpage = int(re.search('/0-(\d+)/', url, re.S).group(1))
        pagegroup = []

        for i in range(nowpage, total_page + 1):
            link = re.sub('/0-(\d+)/', '/0-%s/' % i, url, re.S)
            pagegroup.append(link)

        return pagegroup

    def getsource(self, url):
        html = requests.get(url)
        return html.text

    def getclasses(self, source):
        classes = re.search('<ul class="zy_course_list">(.*?)</ul>', source, re.S).group(1)
        return classes

    def geteach(self, classes):
        eachclasses = re.findall('<li>(.*?)</li>', classes, re.S)
        return eachclasses

    def getinfo(self, eachclass):
        info = {}
        info['title'] = re.search('<a title="(.*?)"', eachclass, re.S).group(1)
        info['people'] = re.search('<p class="color99">(.*?)</p>', eachclass, re.S).group(1)
        return info

    def saveinfo(self, classinfo):
        f = open('info.txt', 'a')

        for each in classinfo:
            f.writelines('title : ' + each['title'] + '\n')
            f.writelines('people : ' + each['people'] + '\n\n')

        f.close()


if __name__ == '__main__':

    classinfo = []
    url = 'http://www.maiziedu.com/course/list/all-all/0-1/'
    maizispider = spider()
    all_links = maizispider.changePage(url, 30)
    for each in all_links:
        htmlsources = maizispider.getsource(each)
        classes = maizispider.getclasses(htmlsources)
        eachclasses = maizispider.geteach(classes)

        for each in eachclasses:
            info = maizispider.getinfo(each)
            classinfo.append(info)

    maizispider.saveinfo(classinfo)
