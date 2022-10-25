import csv
import os
import requests
from bs4 import BeautifulSoup
import shutil

def find_author(pict_id):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 FS"}
    url = "https://www.pixiv.net/artworks/"+pict_id[0]
    
    r = requests.get(url=url, headers=headers)
    # r.encoding = r.apparent_encoding
    r.encoding = 'utf-8'
    # print("状态：", r.raise_for_status, r.apparent_encoding)
    text = r.text
    
    soup = BeautifulSoup(text, 'html.parser')
    data_sp = soup.find_all('meta')[-1]
    false = False
    true = True
    null = None
    data = list(eval(data_sp.get('content'))['illust'].values())[0]
    info_dict = {'pict_id':data['illustId'],
                 'authorName':data['userName'],
                 'authorId':data['userId'],
                 'original':data['urls']['original'],
                 'loacl':"file:///c:/Users/25315/Desktop/文件/图片/pixiv/"+pict_id[0]+'_p0.'+pict_id[1]}
    return info_dict

if __name__=='__main__':
    root_path = "C:\\Users\\25315\\Desktop\\文件\\图片\\pixiv\\"
    temp_path = root_path+"temp\\"
    record_path = root_path+"file\\record.csv"

    pict_id_list = list(map(lambda x:x.split('_p0.'), os.listdir(temp_path)))
    print(pict_id_list)

    with open(record_path, 'a', encoding='utf-8', newline='') as f:
        for i in pict_id_list:
            info_dict = find_author(i)
            # print(info_dict)
            wr = csv.writer(f)
            wr.writerow(info_dict.values())
            shutil.move(temp_path+i[0]+'_p0.'+i[1], root_path)