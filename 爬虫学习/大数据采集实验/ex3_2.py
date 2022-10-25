from matplotlib import pyplot as plt
import csv
import winreg
import os
from datetime import datetime

def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders')
    return winreg.QueryValueEx(key, 'Desktop')[0]
desktop_path = get_desktop()

date, max_tem, min_tem = [], [], []
file_list = os.listdir(desktop_path+'\\weather_info\\武汉')
file_list.sort(key=lambda s:int(s[-6:-4]))
for i in file_list:
    with open(desktop_path+'\\weather_info\\武汉\\'+i, 'r', encoding='utf-8') as f:
        text = csv.reader(f)
        for line in text:
            line[0] = datetime.strptime(line[0][:10], '%Y-%m-%d')
            line = line[:3]
            line[1] = int(line[1][:-1])
            line[2] = int(line[2][:-1])
            date.append(line[0])
            max_tem.append(line[1])
            min_tem.append(line[2])
#             weather_data.append(line)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig = plt.figure(dpi=128, figsize=(10,6))
head_title = ['日期', '最高温度', '最低温度']
plt.title("武汉4到6月温度", fontsize=24)
plt.xlabel('', fontsize=26)
plt.ylabel("温度℃", fontsize=16)
plt.plot(date, max_tem, c='red')
plt.plot(date, min_tem, c='blue')
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
# for i in weather_data:
#     print(i)