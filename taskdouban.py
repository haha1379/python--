import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
    }


for i in range(0,10):
    url = "https://movie.douban.com/top250?"+"start="+str(i*25)+"&filter="
    #print(url)
    res = requests.get(url,headers = headers)
    #print(res.status_code)
    soup = BeautifulSoup(res.content,'html.parser')
    target = soup.select('#content > div > div.article > ol > li > div > div.pic > a > img')
    for film in target:
        print(film.get('alt'),2*'#',film.get('src'))
