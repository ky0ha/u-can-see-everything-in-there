# -*- coding: utf-8 -*- #

# --------------------------------------------
# File Name:                SRTF simulate
# Author:                   ky0ha
# Version:                  ver0_1
# Created:                  2021/6/3
# Description               Main Function:      模拟短进程优先SJF算法
# Function List:            exit()
# History:
#       <author>        <version>       <time>      <desc>
#       ky0ha           ver0_1          2021/6/3    create, write

class time:
    def __init__(self, hour=None, minute=None):
        self.hour = hour
        self.minute = minute

    def compute_total(self):
        self.total = hour*60 + minute

    def increase(self, minute):
        self.total += minute

    def different(self, minute):
        self.total -= minute

class SJF:
    def __init__(self, value):
        super().__init__()
        self.name = self.__getName(value[0])
        self.arrive = self.__getArrive(value[1])
        self.zx = self.__getZx(value[2])
        self.ram = self.__getRam(value[3])
        self.jobTime = time()
        self.processTime = time()
        self.finishTime = time()
        self.zz = None
        self.zzxs = None

    def __getName(self, value):
        return value
    
    def __getArrive(self, value):
        h, m = map(int, value.split(':'))
        return time(h, m)
    
    def __getZx(self, value):
        return int(value)
    
    def __getRam(self, value):
        return int(value)
    
def default_data():
    return [['JOB1', '8:06', 42, 55],
            ['JOB2', '8:20', 30, 40],
            ['JOB3', '8:30', 24, 15],
            ['JOB4', '8:36', 15, 25],
            ['JOB5', '8:42', 12, 20]]

def init_data_list(value):
    return [SJF(item) for item in value]

def print_list(ls):
    for i in ls:
        print("{:^4}\t{:>2}:{:0>2}\t{:^3}\t{:^2}".format(i.name, i.arrive.hour, i.arrive.minute, i.zx, i.ram))

def print_result(ls):
    for i in ls:
        print("{:^4}\t{:>2}:{:0>2}\t{:^3}\t{:>2}:{:0>2}\t{:>2}:{:0>2}\t{:>2}:{:0>2}\t{:>3}\t{:.2f}".format(i.name, i.arrive.hour, i.arrive.minute, i.zx, i.jobTime.hour, i.jobTime.minute, i.processTime.hour, i.processTime.minute, i.finishTime.hour, i.finishTime.minute, i.zz, i.zzxs))

recourse = default_data()
recourse = init_data_list(recourse)
print_list(recourse)
def calculation(ls):
    wating_list = []