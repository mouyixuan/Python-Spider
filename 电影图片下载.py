'''
爬取最新电影排行榜单
url：http://dianying.2345.com/top/
使用 requests --- bs4 线路
Python版本： 3.6
OS： mac os 10.10.5
'''

import requests
import bs4

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status
        # 该网站采用gbk编码！
        r.encoding = 'gbk'
        return r.text
    except:
        return "someting wrong"

def get_content(url):
    html = get_html(url)
    soup = bs4.BeautifulSoup(html, 'lxml')
    movies_list = soup.find('ul', class_='picList clearfix')
    movies = movies_list.find_all('li')
    for top in movies:
        img_url=top.find('img')['src']
        name = top.find('span',class_='sTit').a.text
        actors = top.find('p',class_='pActor')
        actor= ''
        for act in actors.contents: 
            actor = actor + act.string +'  '
        #找到影片简介
        intro = top.find('p',class_='pTxt pIntroShow').text
        print("片名：{}\n{}\n{} \n \n ".format(name,actor,intro) )
        #把图片下载下来存储到img文件夹：
        with open('/Users/xiejinlun/Desktop/img/'+name+'.png','wb+') as f:
            f.write(requests.get("http:"+img_url.split("jpg")[-2]+"jpg").content)

def main():
    url = 'http://dianying.2345.com/top/'
    get_content(url)

if __name__ == "__main__":
    main()