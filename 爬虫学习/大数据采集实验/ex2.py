import requests
from bs4 import BeautifulSoup

# 配置头信息以及url链接
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 FS"}
city = input('输入城市名拼音：')
url = f"http://lishi.tianqi.com/{city}/201807.html"

# 创建一个 requests 对象，内容是返回的报文
r = requests.get(url=url, headers=headers)
# 重编码
r.encoding = r.apparent_encoding
# 打印 requests 状态
print("状态：", r.raise_for_status)
# 返回 requests 的文本形式，即 html 页面内容
text = r.text

# 创建一个 bs4 对象，解析方式为 html.parser，解析内容为text
soup = BeautifulSoup(text, 'html.parser')
# 获得所有的 ul 标签，并且标签的 class 为 'thrui'
data_sp = soup.find('ul', class_='thrui')
# 以文本形式返回找到的 ul 标签的内容
data = data_sp.get_text()

# 根据 ul 标签返回的文本内容的特征进行总体的分割，分割后数组的各元素为某天的日期、最高气温、最低气温、天气、风向
data = data.split('\n\n\n\n')
# 创建一个空数组便于分割 data 数组内每一个元素，并使其变为一个二维数组存放在 result 内
result = []
# 遍历整个数组
for i in data:
    # temp 用以存放某一天的天气信息
    temp = []
    # 进一步清理数据并存入 temp 数组
    for j in i.split('\n'):
        if j!='':
            temp.append(j)
    # 每次每个元素处理完毕之后将处理后生成的数组加入到 result 数组内
    result.append(temp)
# 删除最后一个数组的最后一个内容，其为无关内容'显示更多'
del result[-1][-1]

# for i in result:
#     print(i)
# 输出结果
print("日期\t最高气温\t最低气温")
# max_tem 存放最高气温的索引
max_tem = 0
for index, value in enumerate(result):
    print("{}\t{}\t{}".format(value[0], value[1], value[2]))
    if int(value[1][:-1])>max_tem:
        # 更新最高温度的索引
        max_tem = index
print("本月最高气温在 {} 这天，最高温度达到 {}".format(result[max_tem][0], result[max_tem][1]))