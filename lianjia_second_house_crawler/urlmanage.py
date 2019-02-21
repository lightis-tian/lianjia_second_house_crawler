# -*- coding:UTF-8 -*-

class UrlManager():
    #import _pickle as p

    def __init__(self,filename):
        self.new_urls = open(filename,'a+')

    def dump_target_url(self,url):    #将待爬取的url追加写入文件
        dump_url = self.new_urls.write(url)

    def close_file(self):
        self.new_urls.close()

    