import matplotlib.pyplot as plt

def a(n):
    if n%2==1:
        return (pow(n,2)+3*n+4)/(2*n+4)
    else:
        return (pow(n,2)+4*n+4)/(2*n+4)

x = [i for i in range(256)]
y = list(map(a, x))

plt.figure()
plt.plot(x, y)
plt.show()