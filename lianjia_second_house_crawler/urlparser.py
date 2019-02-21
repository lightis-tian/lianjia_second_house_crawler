# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
#from dataoutput import DataOutput

class UrlParser():
    
    def __init__(self,url,headers):
        self.url = url
        self.headers = headers

    def get_url_soup(self):
        url_text = requests.get(self.url,headers = self.headers,timeout = (3,5)).text
        global url_soup
        url_soup = BeautifulSoup(url_text,'html.parser')
        return url_soup

    #获取详情href
    def get_url_href(self,url_soup):    
        href_list = []
        s = url_soup.find_all('a',class_ = "noresultRecommend img ")
        for one in s:
            href = str(one['href'])
            href_list.append(href)
        return href_list

    #获取首行信息
    def get_first_row(self,detail_soup):
        first_row = []
        soup_first_row = detail_soup.find_all('span',class_ = "label")
        for sth in soup_first_row:
            sth = sth.string
            first_row.append(sth)
        first_row.remove('看房时间')
        first_row.remove('链家编号')
        first_row.insert(2,'房屋总价')
        return first_row

    #获取价格信息
    def get_price(self,detail_soup):
        price = detail_soup.find('span',class_ = 'total').string
        return price    

    #获取附近情况信息
    def get_around_info(self,detail_soup):
        around_info = []
        communityname = detail_soup.find('a',class_ = 'info',target = '_blank').string
        areaname = detail_soup.find('a',class_="supplement").string
        around_info.append(communityname)
        around_info.append(areaname)
        return around_info

    #获取基本属性信息
    def get_base_info(self, detail_soup):    
        second_house_bace_info = []
        soup_base_info = detail_soup.find_all('div', class_ = "base")[0].find_all('li')
        for one in soup_base_info:
            one = str(one)[35:len(one)-7]
            second_house_bace_info.append(one)
        return second_house_bace_info

    #获取交易属性信息
    def get_transaction(self, detail_soup):
        second_house_transaction = []
        soup_transaction = detail_soup.find_all('div',class_ = 'transaction')[0].find_all('span')
        for two in soup_transaction:
            two = str(two.string).strip()
            second_house_transaction.append(two)
        second_house_transaction =  second_house_transaction[1:len(second_house_transaction):2]
        return second_house_transaction
    
