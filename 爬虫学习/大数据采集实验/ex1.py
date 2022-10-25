import requests
import json
from bs4 import BeautifulSoup
import re
import os
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 FS"}

def get_html(url):
    r = requests.get(url=url, headers=headers)
    # 获得一个 requests 对象，请求目标为传入的 url 参数，并使用预设的 headers 伪造报头
    r.encoding = r.apparent_encoding
    print("状态: ", r.raise_for_status)
    # r.raise_for_status 为 requests 对象的一个属性，表明请求的状态结果，成功则为200
    return r.text
    # 返回对象 r 的文本内容

def get_json(url):
    r = requests.get(url=url, headers=headers)
    r.encoding = r.apparent_encoding
    print("状态: ", r.raise_for_status)
    return r.json()

def get_url_list(json_text):
    url_dict = dict()
    for each in json_text['searchVO']['catMap']['gongwen']['listVO']:
        url_dict[each['url']] = each['title'].replace('<em>','').replace('</em>','')
    for each in json_text['searchVO']['catMap']['otherfile']['listVO']:
        url_dict[each['url']] = each['title'].replace('<em>','').replace('</em>','')
    return url_dict

def get_all_link():
    url_dict = dict()
    for i in range(3):
        url=f'http://sousuo.gov.cn/data?t=zhengce&q=%u5916%u8D38&timetype=timeqb&mintime=&maxtime=&sort=&sortType=1&searchfield=title&pcodeJiguan=&childtype=&subchildtype=&tsbq=&pubtimeyear=&puborg=&pcodeYear=&pcodeNum=&filetype=&p={i}&n=5&inpro='
        json_text = get_json(url)
        dic = get_url_list(json_text)
        if not dic:
            break
        url_dict.update(dic)
    return url_dict

def save_file(url, title):
    text = get_html(url)
    soup = BeautifulSoup(text, 'html.parser')
    fp = open(f'../file/{title}.txt', 'w', encoding='utf-8')
    for each in soup.find_all('p'):
        if each.string:
            fp.writelines(each.string)
    fp.close()
    print("写入成功")

def main():
    if not os.path.exists('../file/'):
        os.makedirs('../file/')
    url_dict = get_all_link()
    for url in url_dict:
        save_file(url, url_dict[url])

main()