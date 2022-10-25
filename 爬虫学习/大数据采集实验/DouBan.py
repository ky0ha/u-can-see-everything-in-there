# 爬取豆瓣电影的短评
# 例如：https://movie.douban.com/subject/26588308/comments

# 1.输入一个豆瓣电影的短篇界面，获取评论内容。
# 2.爬取遇到下一页时，能够自动翻页获取下页内容。
# 3.将获取到的内容按照utf-8解析，并且写入到comment.txt中，一个短评一行。

import requests # 请求库，用于发送 get 请求到要爬取的页面地址
from bs4 import BeautifulSoup   # html 文本处理库，处理爬取到的文本
import random   # 随机库，随机选取 user_agent 和代理 ip
import winreg   # windows 的注册表库，用于获取桌面路径

def get_desktop():
    # 获取桌面路径
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders')
    return winreg.QueryValueEx(key, 'Desktop')[0]
# 存储桌面路径到变量
desktop_path = get_desktop()

# user_agent 表，用于更换 user_agent
USER_AGENTS = [
    "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1"
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12 "
]
# ip 代理表
IP_AGENTS = [
    "http://58.240.53.196:8080",
    "http://219.135.99.185:8088",
    "http://117.127.0.198:8080",
    "http://58.240.53.194:8080"
]
# 设置代理
proxies = {"http": random.choice(IP_AGENTS)}

# 设置要爬取的影评网站 absolute 和请求包的报头 headers
absolute = "https://movie.douban.com/subject/26588308/comments"
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

comment_list = []   # 评论表，存放爬取下来的评论字符串
next_page = ''  # 下一个页面的链接，实现自动爬取下一页内容
# 爬取循环
while True:
    r = requests.get(url=absolute+next_page, headers=headers)   # 发送 get 请求，并将得到的内容对象存入变量
    text = r.text   # 以文本的形式返回请求到的内容
    print(r.raise_for_status)   # 输出请求状态信息，200 为成功
    data = BeautifulSoup(text, "html.parser")   # 创建一个对请求到的文本内容进行 html.parser 解析的对象
    # 找到所有的评论的标签，并将其以字符串的形式存入 comment_list
    for tag in data.find_all('span', class_='short'):
        comment_list.append(tag.get_text())
    # 当取不到下一页的链接内容的时候，结束循环
    try:
        next_page = data.find('a', class_='next').get('href')
    except AttributeError:
        break

# 保存文件到桌面的 豆瓣影评.txt 内，每次保存的时候会覆盖原先的内容
with open(desktop_path+'\\豆瓣影评.txt', 'w', encoding='utf-8') as f:
    for comment in comment_list:
        f.write(comment+'\n\n') # 两个 \n 实现评论与评论之间隔一行，便于阅览