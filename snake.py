n = int(input())
if not isinstance(n, int):print([])
d = iter(range(n ** 2))
a = r = [[[x, y] for y in range(n)] for x in range(n)]
while a:
    for x, y in a[0]: r[x][y] = next(d) + 1
    a = list(zip(*a[1:]))[::-1]
for i in r:
    print(i)