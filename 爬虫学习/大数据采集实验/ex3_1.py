from 可视化天气爬虫.weather_catcher import *
import csv
import os
import winreg

def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders')
    return winreg.QueryValueEx(key, 'Desktop')[0]
desktop_path = get_desktop()

searching_list_city = ['南昌', '长沙', '武汉', '合肥', '广州']
searching_list_date = ['202104', '202105', '202106']

if not os.path.exists(desktop_path+'\\weather_info'):
    os.mkdir(desktop_path+'\\weather_info')
save_path = desktop_path + '\\weather_info'

for i in searching_list_city:
    if not os.path.exists(save_path+'\\'+i):
        os.mkdir(save_path+'\\'+i)
    for j in searching_list_date:
        search = weather_catcher(city=i, date=j)
        result = search.getListFromLink()
        with open(save_path+'\\'+i+'\\'+j+'.csv', 'a', encoding='utf-8',newline='') as f:
            wr = csv.writer(f)
            wr.writerows(result)
            print('writed! {}, {} in path: {}'.format(i, j, save_path+'\\'+i+' '+j))



