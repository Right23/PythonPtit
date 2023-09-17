from math import*
def snt(x):
    if x<2:
        return 0
    for i in range(2, isqrt(x)+1, 1):
        if x%i==0:
            return 0
    return 1

n=int(input())
a = [int(i) for i in input().split()]
se = {}
for i in a:
    if i in se:
        se[i]+=1
    else:
        se[i] = 1
for i in se:
    if snt(i):
        print(i, se[i], sep=' ')

