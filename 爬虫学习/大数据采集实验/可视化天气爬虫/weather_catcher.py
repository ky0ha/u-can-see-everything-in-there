from bs4.builder import TreeBuilder
import requests
from bs4 import BeautifulSoup

class weather_catcher:
    '''
    通过默认的url获得天气数据
    方法列表：
        __init__：初始化函数
        getCity：获取城市名
        getDate：获取日期
        __isExistsCity：判断是否为有效城市
        getListFromLink：获取城市在某一月的天气信息
        showResult：输出结果
    参数列表：
        headers：字典，requests使用的报头信息，包含User-Agent客户端信息
        url：字符串，表示天气获取的网站
        city：字符串，表示查询的目标城市名
        date：字符串，表示查询的日期，格式为"yyyymm"
        is_date_ready：布尔值，表示日期是否可以使用
        link：字符串，表示处理完之后的具体查询某一月某个城市温度的url
        queryAddress：列表，存放带爬取url
        result：二维数组，存放天气查询结果
    '''
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 FS"}
    url="http://lishi.tianqi.com/"

    def __init__(self, **kwargs):
        '''
        初始化函数，获取城市和日期信息并创建爬取具体的网址
        '''
        if kwargs['city'] and kwargs['date']:
            self.city = kwargs["city"]
            if kwargs['date'].isdecimal():
                self.is_date_ready = True
                self.date = kwargs['date']
        else:
            self.city = self.getCity()  # 获取城市名
            self.is_date_ready = False  # 初始化是否是可用日期的布尔值
            self.date = self.getDate()  # 获取日期

        # 创建具体的爬取链接
        if self.__isExistsCity() and self.is_date_ready:    # 如果是可用城市名
            # 通过字符串拼接创建具体链接并显示，例如 "http://lishi.tianqi.com/wuhan/201908.index"
            self.link = self.url + self.link.split('/')[0] + '/' + self.date + '.html'
            print("the link is : " + self.link)
    
    def getCity(self):
        '''
        获取城市名
        '''
        return input("请输入想要查找的城市：")
    
    def getDate(self):
        '''
        获取日期
        '''
        date = input("请输入想要查找的日期（yyyymm)，直接输入enter取消输入：")
        while date:
            if date.isdecimal():    # 判断是否是数字字符串
                self.is_date_ready = True
                return date
            else:
                print("日期输入错误，请重新输入，直接输入enter取消输入：")
    
    def __isExistsCity(self):
        '''
        判断是否是存在的城市名
        '''
        # 获取 http://lishi.tianqi.com/ 主页的信息
        addresses = BeautifulSoup(requests.get(url=self.url, headers=self.headers).text, "html.parser")
        # 在主页返回的 html 文件内查找是否存在字符串 city
        self.queryAddress = addresses.find('a',text=self.city)
        if self.queryAddress:
            # 如果存在字符串 city，则取对应的链接并存入 link，返回 True， 反之返回 False
            self.link = self.queryAddress["href"]
            return True
        else:
            return False
    
    def getListFromLink(self):
        '''
        获取城市在某一月的天气信息
        '''
        # 使用一行直接获取到对应天气的未处理的数据
        data_dirty = BeautifulSoup(requests.get(url=self.link, headers=self.headers).text, "html.parser").find('ul', class_='thrui').get_text()
        
        # 根据 ul 标签返回的文本内容的特征进行总体的分割，分割后数组的各元素为某天的日期、最高气温、最低气温、天气、风向
        data_dirty = data_dirty.split('\n\n\n\n')
        # 创建一个空数组便于分割 data 数组内每一个元素，并使其变为一个二维数组存放在 result 内
        self.result = []
        for i in data_dirty:
            temp = []   # temp 用以存放某一天的天气信息
            for j in i.split('\n'): # 进一步清理数据并存入 temp 数组
                if j!='':
                    temp.append(j)
            self.result.append(temp)    # 每次每个元素处理完毕之后将处理后生成的数组加入到 result 数组内
        del self.result[-1][-1] # 删除最后一个数组的最后一个内容，其为无关内容'显示更多'
        return self.result
    
    def showResult(self):
        '''
        输出结果
        '''
        print("日期\t\t\t最高气温\t最低气温")
        # max_tem 存放最高气温的索引
        max_tem = 0
        for index, value in enumerate(self.result):
            print("{}\t{}\t\t{}".format(value[0], value[1], value[2]))
            if int(value[1][:-1])>max_tem:
                # 更新最高温度的索引
                max_tem = index
        print("本月最高气温在 {} 这天，最高温度达到 {}".format(self.result[max_tem][0], self.result[max_tem][1]))

# test = weather_catcher()
# test.getListFromLink()
# test.showResult()