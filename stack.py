class Stack(object):
    """栈"""
    def __init__(self):
        self.items = []
        self.length = 0

    def is_empty(self):
        """判断是否为空"""
        return self.length == 0

    def push(self, item):
        """加入元素"""
        self.items.append(item)
        self.length += 1

    def pop(self):
        """弹出元素"""
        self.length -= 1
        return self.items.pop()

    def peek(self):
        """返回栈顶元素"""
        return self.items[len(self.items)-1]

    def size(self):
        """返回栈的大小"""
        return self.length