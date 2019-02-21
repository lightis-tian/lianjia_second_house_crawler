# -*- coding: UTF-8 -*-


import requests
from bs4 import BeautifulSoup
import csv

header ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/65.0'}

#将待爬取的url写入new_url.text文件
with open('new_url.txt','a+') as new_url:
    for i in range(1,101):
        if i == 1:
            target_url = 'https://sh.lianjia.com/ershoufang/'
        else:
            target_url = 'https://sh.lianjia.com/ershoufang/' + 'pg' + str(i) + '/'
        new_url.write(target_url + '\n')
    new_url.close()


#获取详情href
url = open('new_url.txt','r').readlines()
for line in url:
    line = line.strip('\n')
    url_soup = requests.get(line,headers = header).text
    s = BeautifulSoup(url_soup,'html.parser')
    s = s.find_all('a',class_ = "noresultRecommend img ")
    with open('new_href.txt','a+') as new_href:
        for one in s:
            href = str(one['href'])
            new_href.write(href + '\n')
        new_href.close()

#获取首行信息
def get_first_row(detail_soup):
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
def get_price(detail_soup):
    price = detail_soup.find('span',class_ = 'total').string
    return price

#获取附近情况信息
def get_around_info(detail_soup):
    around_info = []
    communityname = detail_soup.find('a',class_ = 'info',target = '_blank').string
    areaname = detail_soup.find('a',class_="supplement").string
    around_info.append(communityname)
    around_info.append(areaname)
    return around_info

#获取基本属性信息
def get_base_info(detail_detail_soup):
    second_house_bace_info = []
    soup_base_info = detail_soup.find_all('div', class_ = "base")[0].find_all('li')
    for one in soup_base_info:
        one = str(one)[35:len(one)-7]
        second_house_bace_info.append(one)
    return second_house_bace_info

#获取交易属性信息
def get_transaction(detail_soup):
    second_house_transaction = []
    soup_transaction = detail_soup.find_all('div',class_ = 'transaction')[0].find_all('span')
    for two in soup_transaction:
        two = str(two.string).strip()
        second_house_transaction.append(two)
    second_house_transaction =  second_house_transaction[1:len(second_house_transaction):2]
    return second_house_transaction

f = open('new_href.txt','r').readlines()

csvfile = open('result.csv','w',newline = '')
writer = csv.writer(csvfile)

for detail_url in f:
    i = f.index(detail_url)
    print('正在处理第{}个href'.format(i))
    detail_url = detail_url.strip('\n')
    try:
        detail_text = requests.get(detail_url,headers = header,timeout = (3,5)).text
        detail_soup = BeautifulSoup(detail_text,'html.parser')
    except:
        pass
    if i == 0:
        first_row = get_first_row(detail_soup)
        writer.writerow(first_row)
    price = get_price(detail_soup)
    around_info = get_around_info(detail_soup)
    base_info = get_base_info(detail_soup)
    transaction_info = get_transaction(detail_soup)
    result = around_info + base_info + transaction_info
    result.insert(2,price)
    writer.writerow(result)
    