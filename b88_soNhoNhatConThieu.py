n = int(input())
c = [0]*30001
a = [int(i) for i in input().split()]
for i in a:
    c[i] = 1
k = max(a)
for i in range(1, k+2):
    if c[i]==0:
        print(i)
        break
