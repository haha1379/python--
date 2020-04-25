import requests
import re


def gethtmltext(url):
    kv = {
        'cookie': '',
        'referer': 'https://s.taobao.com/search?q=ipad&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200423&ie=utf8',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
        }
    res = requests.get(url,timeout = 30,headers = kv)
    print(res.status_code)
    res.raise_for_status()
    res.encoding = res.apparent_encoding
    print(res.text)
    return res.text


def parsepage(ulist,html):
    price_list = re.findall(r'\"view_price\"\:"\[\d+\.]*\"',html)
    name_list = re.findall(r'\"raw_title\"\:\".*?\"',html)
    print(len(price_list))
    for i in range(len(price_list)):
        price = eval(price_list[i].split(":")[1])
        name = eval(name_list[i].split(":")[1])
        ulist.append([price,name])
    print(ulist)

def main():
    goods_name = "手机"
    start_url = "https://s.taobao.com/search?q=" + goods_name
    info_list = []
    page = 3
    count = 0
    for i in range(page):
        count += 1
        url = start_url + "&s=" + str(44*i)
        html = gethtmltext(url)
        parsepage(info_list,html)

main()

