class Triangle:
    def __init__(self, x, y, z):
        t = 1.5
        self.a = x
        self.b = y
        self.c = z
        print(t)

    def area(self):
        s = (self.a + self.b + self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**(1.0/2)

    def perimeter(self):
        return self.a + self.b + self.c

t1 = Triangle(6, 6, 6)
print("t1的面积为：", t1.area())
print("t1的周长：", t1.perimeter())

t2 = Triangle(3, 4, 5)
print("t2的面积为：", t1.area())
print("t2的周长：", t1.perimeter())