from math import*
n = int(input())
a=[]
for i in range(n):
    row = input()
    a.append(list(row))
h=[0]*n
c=[0]*n
for i in range(n):
    for j in range(n):
        if a[i][j]=='C':
            h[i]+=1
            c[j]+=1
res = 0
# for i in range(n):
#     print(h[i], sep=' ')
# for i in range(n):
#     print(c[i], sep=' ')
for i in range(n):
    if h[i]>=2:
        res+=comb(h[i], 2)
for i in range(n):
    if c[i]>=2:
        res+=comb(c[i], 2)
print(res)
