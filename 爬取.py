import requests
from lxml import etree
import parsel
import os.path
import csv
import pandas as pd
import time
from datetime import datetime, timedelta
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62',
    'Cookie':'Path=/; Path=/; gkmlfront_session=eyJpdiI6IksyeEpHZXJDOUk2ZWhEb2xuNStpU0E9PSIsInZhbHVlIjoiNExYc1FYVUQ2b2l6c2NxSnhGSEVHdUJiWUttYU0yQzRHM1M3VEZ3M1ZZSE9LOW96YnhqUWdpRkp3Q0pZZFNDRSIsIm1hYyI6ImViNmI3Yjg5MzVlNmUzNjcxZDEzZDJhYzk1ZTQ1MTQ4ZDBiZDgyMzdhNGZmMTU2ZjgxMGViOTAyNzRiYjcwNmIifQ%3D%3D; front_uc_session=eyJpdiI6Im5XUEFyZmRERkxcLzlYdXlOQnhReXp3PT0iLCJ2YWx1ZSI6IkM1VE0zM3VjdG1rK3RBc1Bvcmo4Zjl1WnBJK1lcL0dqZTQ3M1NyeW9raDlrUWpFYm1jYVE4cmVrMjU5YnlHamptIiwibWFjIjoiNzQ3YWQyZTU3YmZiZWViZTE5YjRjMGYyODEwODZlYjVkOWMwMDhjYTVmMjFmMGRlYjIzMWMxYWZlNjdlYzUxOCJ9'
    }
def get_content(url):
    res=requests.get(url)
    res.encoding="utf-8"
    # print(res.text)
    select=parsel.Selector(res.text)
    title=select.css('.content .title::text').get()
    content=select.css('.content .article-content').get()
    with open(title+".html",mode="w",encoding='utf-8')as f:
        f.write(content)
def timeinputAndgetpaper():
    end=[]
    begin=[]
    # 关于时间的表示
    data=pd.read_csv("信息.csv")
    # data["发布日期"].head()
    data_time=[]
    for i in data["发布日期"]:
        data_time.append(i.split(" ")[0])
    data['年月日']=data_time
    print("请你输入事件范围")
    print("开始时间（xxxxxxxx）:\t")
    try:
        time1=input()
        time_begin=pd.to_datetime(time1.split('-')[0]).strftime( '%Y-%m-%d')
        time_end=pd.to_datetime(time1.split('-')[1]).strftime( '%Y-%m-%d')
    except ValueError:  
        print("时间格式错误，请按照(20220101-20230601) 的格式输入")  
    p=0
    for i in data['年月日']:
        p=p+1
    #     结束时间
        if time.strptime(str(i),'%Y-%m-%d')>=time.strptime(str(time_end),'%Y-%m-%d'):
            end.append(p)
        #     开始时间
        if time.strptime(str(i),'%Y-%m-%d')<=time.strptime(str(time_begin),'%Y-%m-%d'):
            begin.append(p)  
    for i in range(end[0]-1,begin[0]):
        url=data["政策正文附件链接"][i]
        get_content(url)
kl=[]
times_all=[]
for i in range(1,50):
    url=f"https://www.gd.gov.cn/gkmlpt/api/all/5?page={i}&sid=2"
    r=requests.get(url,headers=headers)
    data=json.loads(r.text)
    for i in data['articles']:
        suoyin=i['identifier']
        fabu_jigou=i['publisher']
        times=i['created_at']
        title=i['title']
        urls=i['url']
        times_all.append(times)
        kl.append([suoyin,fabu_jigou,times,title,urls])
data1=pd.DataFrame(kl,columns=['收集索引号','发布机构','发布日期','政策标题','政策正文附件链接'])
data1.to_csv("信息.csv")
timeinputAndgetpaper()
