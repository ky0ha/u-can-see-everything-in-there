from random import randint, seed
from time import time
# ls = []
# space, longer, size = map(int, input().split())
# times = space//size
# while times>=64:
#     temp = [randint(0,1) for a in range(64)]
#     ls.append(temp)
#     times-=64
# else:
#     temp = [randint(0,1) for a in range(times)]
#     ls.append(temp)
#     del times
# print(ls)

class pages:
    ls = []
    space, longer, size = 0, 0, 0
    table = []
    free_space = 0
    def __init__(self):
        super().__init__()
        seed(time())
        self.space, self.longer, self.size = map(int, input().split())
        times = self.space//self.size
        while times>=64:
            temp = [randint(0,1) for a in range(self.longer)]
            self.ls.append(temp)
            times-=64
        else:
            temp = [randint(0,1) for a in range(times)]
            self.ls.append(temp)
            del times
        
        for i in self.ls:
            for j in i:
                if j==0:
                    self.free_space+=1

    def print_out(self):
        print('  ', end=' ')
        for i in range(self.longer):
            print("{:^2d}".format(i), end=' ')
        print('\n', end='')

        lines = 0
        for i in self.ls:
            print("{:^2d}".format(lines), end=' ')
            lines+=1
            for j in i:
                print("{:^2d}".format(j), end=' ')
            print('', end='\n')
        
        print("\n空闲块数：{}".format(self.free_space))

    def add(self, new_size, work_id):
        if self.free_space>=new_size:
            ids = 0
            temp = {"work_id" : "{}".format(work_id)}
            print("work_id\t{}".format(work_id), end='\n')
            ids+=1
            for i,row in enumerate(self.ls):
                for j,value in enumerate(row):
                    if new_size>=1 and value==0:
                        self.ls[i][j] = 1
                        temp["{}".format(ids)] = "({},{})".format(i,j)
                        print("{}\t{}".format(ids, i*self.longer+j), end='\n')
                        ids+=1
                        new_size-=1
            print(temp)
            self.table.append(temp)

    def delete(self, work_id):
        temp = {}
        for index, dictory in enumerate(self.table):
            if dictory["work_id"]=="{}".format(work_id):
                temp = dictory
                del self.table[index]
                break
        
        value_list = list(map(eval, temp.values()))[1:]
        print(value_list)
        for value in value_list:
            i, j = value
            self.ls[i][j] = 0

p = pages()
p.print_out()
p.add(20, 27015)
p.delete(27015)