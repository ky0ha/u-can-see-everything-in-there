import os

def found(path, schema, key):
    file_list = os.listdir(path)
    for i in file_list:
        if schema==1:
            if os.path.isdir(path+'\\'+i):
                found(path+'\\'+i, schema, key)
            elif os.path.isfile(path+'\\'+i):
                if key==i[0]:
                    print(path+'\\'+i)
        elif schema==0:
            if os.path.isdir(path+'\\'+i):
                found(path+'\\'+i, schema, key)
            elif os.path.isfile(path+'\\'+i):
                # print(path+'\\'+i)
                if key==i.split('.')[-1]:
                    print(path+'\\'+i)
        

path=r'C:\Users\25315\Desktop\文件\code\onlyVS\python\爬虫学习\大数据采集实验\实验1文件'
schema = int(input('根据文件类型还是文件名首字母查询（0 or 1）：'))
if schema==1:
    key = input('请输入要查找的文件名首字母：')
elif schema==0:
    key = input('请输入要查找的文件类型：')
found(path, schema, key)