from math import sqrt


def snt(n):
    if n < 2:
        return 0
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
n, m = map(int, input().split())
a = []
for i in range(0, n):
    a.append([])
    a[i] = [snt(int(j)) for j in input().split()]
for i in range(0, n):
    for j in range(0, m):
        print(a[i][j], end=' ')
    print()
# print(*a)