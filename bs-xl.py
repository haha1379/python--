import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
    }

url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html"

res = requests.get(url,headers = headers,timeout = 30)
res.raise_for_status()
res.encoding = res.apparent_encoding
print(res.status_code)

soup = BeautifulSoup(res.text,'html.parser')

#tb = soup.select('tbody')
#print(len(tb))

#tr = soup.select('tr')
#print(len(tr))
#for i,t in zip(range(0,3),tr):
    #print(t)


tgx = soup.select("body > div.container > div > div.col-lg-9.col-md-9.col-sm-9.col-xs-12 > div > div.news-blk > div > table > tbody > tr > td:nth-of-type(1)")
tgy = soup.select("body > div.container > div > div.col-lg-9.col-md-9.col-sm-9.col-xs-12 > div > div.news-blk > div > table > tbody > tr > td:nth-of-type(2) > div")
tgz = soup.select('body > div.container > div > div.col-lg-9.col-md-9.col-sm-9.col-xs-12 > div > div.news-blk > div > table > tbody > tr > td:nth-of-type(3)')
#print(len(tgz))
tgv = soup.select("body > div.container > div > div.col-lg-9.col-md-9.col-sm-9.col-xs-12 > div > div.news-blk > div > table > tbody > tr > td:nth-of-type(4)")

print(len(tgx))
#for i,z in zip(range(0,3),tgz):
    #print(z.get_text())

for i ,x,y,z,v in zip(range(0,30),tgx,tgy,tgz,tgv):
    print(x.get_text(),y.get_text(),z.get_text(),v.get_text())
