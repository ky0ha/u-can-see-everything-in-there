import csv
import os

root_path = "C:\\Users\\25315\\Desktop\\文件\\图片\\pixiv\\"
temp_path = root_path+"temp\\"
file_path = root_path+"file\\"

done = list(map(lambda x: x[:-7], os.listdir(temp_path)))
done_file_format = list(map(lambda x: x[-3:], os.listdir(temp_path)))
done_info = dict(zip(done, done_file_format))

temp_info = []
not_done_link_list = []

with open(file_path+"temp_info.csv", 'r', encoding='utf-8') as f:
    r = csv.reader(f)
    for i in r:
        item = {
            'pid': i[0],
            'author': i[1],
            'uid': i[2],
            'original': i[3],
            'local': i[4]
        }
        temp_info.append(item)
    temp_info = temp_info[1:]

for i in temp_info:
    if i['pid'] in done:
        print('done')
        i['original'] = i['original'][:-3]+done_info[i['pid']]
        i['local'] = i['local'][:-3]+done_info[i['pid']]
    else:
        print('not done')
        i['original'] = i['original'][:-3]+"jpg"
        i['local'] = i['local'][:-3]+"jpg"
        not_done_link_list.append(i['original'])

# for i in temp_info:
#     for j in i.values():
#         print(j, end='\t')
#     print()

with open(file_path+"notdone.txt", 'w', encoding='utf-8') as f:
    for i in not_done_link_list:
        f.write(i+'\n')

with open(file_path+"new_info.csv", 'w', encoding='utf-8', newline='') as f:
    wr = csv.writer(f)
    for i in temp_info:
        wr.writerow(i.values())
