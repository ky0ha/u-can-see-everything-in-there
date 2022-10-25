import os
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import sort

root_path = os.path.abspath(os.path.dirname(__file__))

with open(root_path+'\\page3.html', 'r', encoding='utf-8') as f:
    text = f.read()

date = BeautifulSoup(text, 'html.parser')
table = date.find('table', {'class':'datatbl', 'id':'datatbl'}).find('tbody').find_all('tr')

class stock:
    class my_time:
        def __init__(self, ls):
            self.hour = int(ls[0])
            self.minute = int(ls[1])
            self.second = int(ls[2])
            self.total = self.hour*60 + self.minute
        
    def __init__(self, tag):
        print(tag)
        self.submit_time = self.my_time(tag.find('th').text.split(':'))
        try:
            self.status = tag.find('h5').text
        except AttributeError:
            try:
                self.status = tag.find('h6').text
            except AttributeError:
                self.status = tag.find('h1').text
        values = tag.find_all('td')
        self.submit_price = values[0].text
        self.price_difference = values[1].text
        self.turnover_number = int(values[2].text)
        self.turnover_price = int(''.join(i for i in values[3].text.split(',')))
    
    def show(self):
        # print(f'\n成交时间\t成交价\t价格变动\t成交量（手）\t成交额（元）\t性质')
        print(f'{self.submit_time}\t{self.submit_price}\t{self.price_difference}\t{self.turnover_number}\t{self.turnover_price}\t{self.status}')

stock_list = []
for i in table:
    stock_list.append(stock(i))

stock_list_sorted_turnover_price = sorted(stock_list, key=lambda x:x.turnover_price)
# for i in stock_list_sorted_turnover_price:
#     i.show()

max_price, min_price = stock_list_sorted_turnover_price[-1].turnover_price, stock_list_sorted_turnover_price[0].turnover_price

print(f'最大值:{max_price}\t最小值:{min_price}')

def get_avg(ls : list):
    length, up = len(ls), 0
    for i in range(length):
        up += ls[i].turnover_price
    return [up, up/length]

avgs = get_avg(stock_list_sorted_turnover_price)
print(f'总交易额{avgs[0]}\t平均值为{avgs[1]:.2f}')

stock_list_reversed = sorted(stock_list, key=lambda x:x.submit_time.total, reverse=False)
price_pre_minute = {}
for i in stock_list:
    price_pre_minute[f'14:{i.submit_time.minute}'] = price_pre_minute.setdefault(f'14:{i.submit_time.minute}', i.turnover_price) + i.turnover_price

print('每分钟交易额如下：')
x, y = [], []
for key in price_pre_minute.keys():
    print(f'第{key}时间内交易额为：{price_pre_minute[key]}')
    x.append(key)
    y.append(price_pre_minute[key])
x.reverse()
y.reverse()

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.title("每分钟交易额统计")
plt.xlabel('时间', fontsize=24)
plt.ylabel('交易额', fontsize=24)
plt.plot(x, y)
plt.show()
