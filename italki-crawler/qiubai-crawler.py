# ACK: https://piaosanlang.gitbooks.io/spiders/content/03day/section3.6.html

# -*- coding:utf-8 -*-
import urllib
import requests
import re
import chardet
from lxml import etree

page = 2
url = 'http://www.qiushibaike.com/8hr/page/' + str(page) + "/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.8'}

response = requests.get(url, headers=headers)
resHtml = response.text

html = etree.HTML(resHtml)
result = html.xpath('//div[contains(@id,"qiushi_tag")]')
for site in result:
    #print etree.tostring(site,encoding='utf-8')

    item = {}
    imgUrl = site.xpath('./div/a/img/@src')[0].encode('utf-8')
    username = site.xpath('./div/a/@title')[0].encode('utf-8')
    #username = site.xpath('.//h2')[0].text
    content = site.xpath('.//div[@class="content"]')[0].text.strip().encode('utf-8')
    vote = site.xpath('.//i')[0].text
    #print site.xpath('.//*[@class="number"]')[0].text
    comments = site.xpath('.//i')[1].text

    print (imgUrl, username, content, vote, comments)
