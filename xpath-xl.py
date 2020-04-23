from lxml import etree
import requests
import re

url = "http://www.dxy.cn/bbs/thread/626626#626626"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
    }

#获取url的html
res = requests.get(url,headers)

#用lxml解析html
html = etree.HTML(res.text,etree.HTMLParser())

#利用Xpath表达式获取user和content
user = html.xpath('//*/table/tbody/tr/td[1]/div[2]/a')
#user = tree.xpath('//*[@id="post_2"]/table/tbody/tr/td[1]/div[2]/a')
#content = html.xpath('//*/table/tbody/tr/td[2]/div[2]/*/table/tbody/tr/td/text()')
content = html.xpath('//*/table/tbody/tr/td[2]/div[2]/*/table/tbody/tr/td')
#选对标签，上面选到text(),应该选到上一级标签；
#for x in range(0,len(content)):
    #print(content[x].xpath('string(.)'))
#//*[@id="post_2"]/table/tbody/tr/td[2]/div[2]/div[1]/table/tbody/tr/td/br[1]
#//*[@id="post_2"]/table/tbody/tr/td[2]/div[2]/div[1]/table/tbody/tr/td/text()[2]
#//*[@id="post_3"]/table/tbody/tr/td[2]/div[2]/div[1]/table/tbody/tr/td/text()[2]
#//*[@id="post_2"]/table/tbody/tr/td[2]/div[2]/div[1]/table/tbody/tr/td/a

lis = []
for i,ur,ct in zip(range(0,len(user)),user,content):
    print("user_"+str(i+1),user[i].text.strip(),content[i].xpath('string(.)').strip())
    print(100*"*")
    
