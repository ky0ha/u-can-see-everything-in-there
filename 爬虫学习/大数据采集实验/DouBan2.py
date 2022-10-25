import requests
import random
import re
import matplotlib
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from req_config import USER_AGENTS, IP_AGENTS

proxies = {"http": random.choice(IP_AGENTS)}
absolute = "https://movie.douban.com/subject/25845392/comments"
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Cookie': 'douban-fav-remind=1; __gads=ID=24d8310e2082c5fc-22a6d06e4ac50029:T=1608620754:RT=1608620754:R:S=ALNI_MZft4Dpj-iOb0JcjPVRoBzlyeqHLA; viewed="1477390"; gr_user_id=d8d9d2a9-c1f5-424a-8012-fa3c957093a8; ll="118389"; bid=QPFgJOfTUcg; __utmz=30149280.1626189566.4.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0; __utmz=223695111.1637714627.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=30149280.1165141357.1593323941.1637714627.1637718377.6; __utmc=30149280; __utmb=223695111.0.10.1637718377; __utma=223695111.1234959553.1637714627.1637714627.1637718377.2; __utmc=223695111; _pk_ses.100001.4cf6=*; dbcl2="250615200:r+1sEXwTwj4"; ck=aWi4; push_noty_num=0; push_doumail_num=0; __utmv=30149280.25061; __utmb=30149280.16.10.1637718377; _vwo_uuid_v2=D166A748FEBD67C1F5965541B0EFC065D|0c7e670c6f177c8e5124dac18cb7d26e; __yadk_uid=lMsU8gJeQVEzR4TJ65WE9Ro1FLHMhOa9; _pk_id.100001.4cf6=9955d86c322ef83b.1637714626.2.1637719983.1637715586.',
           'Host': 'movie.douban.com',
           'sec-ch-ua': '\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"',
           'sec-ch-ua-mobile': '?0',
           'sec-ch-ua-platform': "Windows",
           'Sec-Fetch-Dest': 'document',
           'Sec-Fetch-Mode': 'navigate',
           'Sec-Fetch-Site': 'same-origin',
           'Sec-Fetch-User': '?1',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': random.choice(USER_AGENTS)
           }


def get_data(absolute: str, headers: dict):
    total, next_page, rating_counter = 0, '', {}
    while total < 100:
        r = requests.get(url=absolute+next_page, headers=headers)
        text = r.text
        print(r.raise_for_status)
        data = BeautifulSoup(text, "html.parser")
        for tag in data.find_all('span', attrs={'class': re.compile(r'^allstar\d0\srating$')}):
            rating_counter[tag.get('class')[0]] = rating_counter.setdefault(
                tag.get('class')[0], 0) + 1
            total += 1  # 记录100条信息
            if total > 100:
                break
    return rating_counter   # 返回统计字典


def show(data: dict):
    font = {'family': 'KaiTi',
            'weight': 'bold',
            'size': 12}
    matplotlib.rc("font", **font)

    trans = {'allstar10': '一星', 'allstar20': '二星',
             'allstar30': '三星', 'allstar40': '四星', 'allstar50': '五星'}
    x, labels = [], []
    for key, value in sorted(data.items(), key=lambda x: x[0]):
        x.append(value)
        labels.append(trans[key])

    fig = plt.figure()  # 创建窗口
    plt.pie(x, labels=labels)   # 创建饼图
    plt.title('长津湖评论分级')  # 设置饼图的标题

    plt.show()  # 显示饼图

data = get_data(absolute, headers)
show(data)
