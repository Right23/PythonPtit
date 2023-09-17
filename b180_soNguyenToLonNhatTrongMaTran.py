from math import*
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
n, m = map(int, input().split())
a = []
for i in range(n):
    row = [int(i) for i in input().split()]
    a.append(row)
res = 0
for i in range(n):
    for j in range(m):
        if snt(a[i][j]):
            res = max(res, a[i][j])
if res==0:
    print("NOT FOUND")
else:
    print(res)
    for i in range(n):
        for j in range(m):
            if a[i][j] ==res:
                print("Vi tri ["+str(i)+"]["+str(j)+"]")
