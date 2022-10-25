from itertools import combinations, permutations

class proper(object):
    '''
    手动实现的幂集和全排列方法
    返回幂集：comb
    返回全排列：perm
    '''
    def __init__(self, arr):
        '''
        获取数组，并存储必要的变量
        arr：数组本体
        n：数组长度
        __result：由于全排列使用递归方式，需要一个全局变量存储结果
        '''
        self.arr = arr
        self.n = len(arr)
        self.__result = []
    
    def comb(self):
        '''
        使用二进制法生成幂集，返回一个迭代器
        '''
        for i in range(1 << self.n):    # 1 左移 n 位，等于 2^n
            # temp = []
            # for j in range(self.n):   # j 表示二进制的第 j+1 位
            #     if i & (1<<j):    # 如果 i 的二进制的第 j+1 位是 1，则将对应数字加入结果
            #         temp.append(self.arr[j])
            # yield temp
            yield [self.arr[j] for j in range(self.n) if i & (1<<j)]    # 分解写如上注释所示

    def __create_perm(self, arr, next):
        '''
        递归方法全排列
        next 表示已经确认排列完成的在第几位
        '''
        if next == len(arr)-1:  # 如果到最后一位，也就是所有的都确认排列完成，则添加结果
            self.__result.append(arr)
        else:
            for i in range(next, len(arr)): # 遍历数组的第 next 到结尾
                temp = arr.copy()   # 深复制，避免影响之前的结果
                temp[i], temp[next] = temp[next], temp[i]   # 交换第 i 位和第 next 位
                self.__create_perm(temp, next+1)    # 往深处递归，已经确认排列好的部分 +1

    def perm(self):
        '''
        返回全排列的结果——一个可迭代列表
        '''
        self.__create_perm(self.arr, 0)
        return self.__result

class cheater(object):
    '''
    使用 python 自带的 itertools 库进行幂集、全排列，虽然有效果但是并非手动实现，意义有限
    '''
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
    
    def comb(self):
        for i in range(self.n):
            for j in combinations(self.arr, i):
                yield j
    
    def perm(self):
        return permutations(self.arr, self.n)

l = [1, 2, 3, 4]
test = proper(l)
print("\n".join(str(i) for i in test.comb()))
print("\n".join(str(i) for i in test.perm()))
