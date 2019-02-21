# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import csv


'''
header = {'User-Agent':	'Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/65.0'}
#抓取target_url1
def get_target_url(target_url1):
    get_url = []
    for i in range(1,101):
        if i == 1:
            target_url1 = 'https://sh.lianjia.com/ershoufang/'
        else:
            target_url1 = 'https://sh.lianjia.com/ershoufang/' + 'pg' + str(i) + '/'
        get_url.append(target_url1)
    return get_url

#获得target_url的页面源代码
def get_target_url_text(get_url,header):
    global url_text
    for url in get_url:
        url_text = requests.get(url,headers = header).text
        return url_text

#获得每个页面的详情url-target_url2
target_url2 = []
def get_target_herf(url):
    s = BeautifulSoup(url_text,'html.parser')
    s = s.find_all('a',class_ = "noresultRecommend img ")
    for one in s:
        href = str(one['href'])
        target_url2.append(href)

#对target_url2中的各个url的需要数据进行爬取
def get_detail_soup(target_url2):
    for urls in target_url2:
        url_text = get_target_url_text(urls,header)
        global detail_soup
        detail_soup = BeautifulSoup(url_text,'html.parser')        

'''
urls = 'https://sh.lianjia.com/ershoufang/107000126417.html'
header = {'User-Agent':	'Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/65.0'}
url_text =requests.get(urls,headers = header).text
detail_soup = BeautifulSoup(url_text,'html.parser')


#获取首行
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
print(get_first_row(detail_soup))

#获取价格信息
def get_price(detail_soup):
    price = detail_soup.find('span',class_ = 'total').string
    return price
price = get_price(detail_soup)

#获取基本属性信息
def get_base_info(detail_detail_soup):
    second_house_bace_info = []
    soup_base_info = detail_soup.find_all('div', class_ = "base")[0].find_all('li')
    for one in soup_base_info:
        one = str(one)[35:len(one)-7]
        second_house_bace_info.append(one)
    return second_house_bace_info
base_info =  get_base_info(detail_soup)

#获取交易属性信息
def get_transaction(detail_soup):
    second_house_transaction = []
    soup_transaction = detail_soup.find_all('div',class_ = 'transaction')[0].find_all('span')
    for two in soup_transaction:
        two = str(two.string).strip()
        second_house_transaction.append(two)
    second_house_transaction =  second_house_transaction[1:len(second_house_transaction):2]
    return second_house_transaction
transaction_info =  get_transaction(detail_soup)

#获取附近情况信息
def get_around_info(detail_soup):
    around_info = []
    communityname = detail_soup.find('a',class_ = 'info',target = '_blank').string
    areaname = detail_soup.find('a',class_="supplement").string
    around_info.append(communityname)
    around_info.append(areaname)
    return around_info
around_info = get_around_info(detail_soup)

abc = around_info + base_info + transaction_info 
abc.insert(2,price)
print(abc)

'''
<span class="info">具体信息请致电经纪人</span>
<a href="https://sh.lianjia.com/ditiefang/li143685066s100022041/" class="supplement" title="近11号线(迪士尼-花桥)云锦路站" style="color:#394043;">近11号线(迪士尼-花桥)云锦路站</a>
with open('demo.csv','w',newline = '') as f:
    aaa = csv.writer(f)
    aaa.writerow(abc)
'''


    


