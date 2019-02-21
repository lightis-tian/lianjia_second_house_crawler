# -*- coding:UTF-8 -*-

from urlmanage import UrlManager
from urlparser import UrlParser
from dataoutput import DataOutput

header ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/65.0'}

url_to_file = UrlManager('url.txt')

#将url写入'url.txt'文档
for i in range(1,3):
    if i == 1:
        target_url = 'https://sh.lianjia.com/ershoufang/'
    else:
        target_url = 'https://sh.lianjia.com/ershoufang/' + 'pg' + str(i) + '/'
    url_to_file.dump_target_url(target_url + '\n')
url_to_file.close_file()

#从文档中读取url
urls = open('url.txt','r').readlines()
#print(urls)

#从url中获取href并写入txt文件
header ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/65.0'}
for url in urls:
    url = url.strip('\n')
    url_soup = UrlParser(url,header).get_url_soup()
    s = UrlParser(url,header).get_url_href(url_soup)
    for item in s:
        href_to_txt = DataOutput(item).data_to_txt('href.txt')

#从href.txt文件中读取href并解析
f = open('href.txt','r').readlines()

for detail_href in f:
    i = f.index(detail_href)
    print('正在处理第{}个href'.format(i))
    detail_url = detail_href.strip('\n')
    try:
        global detail
        detail = UrlParser(detail_href,header)
        detail_soup = detail.get_url_soup()
    except:
        pass
    if i == 0:
        first_row = detail.get_first_row(detail_soup)
        DataOutput(first_row).data_to_csv('result_csv.csv')
    price = detail.get_price(detail_soup)
    around_info = detail.get_around_info(detail_soup)
    base_info = detail.get_base_info(detail_soup)
    transaction_info = detail.get_transaction(detail_soup)
    result = around_info + base_info + transaction_info
    result.insert(2,price)
    DataOutput(result).data_to_csv('result_csv.csv')
    
