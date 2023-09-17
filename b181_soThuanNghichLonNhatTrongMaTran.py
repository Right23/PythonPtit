from math import*
def checkTN(n):
    if n < 10:
        return False
    tmp = n
    rev = 0
    while(n>0):
        rev = rev*10+n%10
        n//=10
    return rev==tmp

n, m = map(int, input().split())
a = []
for i in range(n):
    row = [int(i) for i in input().split()]
    a.append(row)
res = 0
for i in range(n):
    for j in range(m):
        if checkTN(a[i][j]):
            res = max(res, a[i][j])
if res==0:
    print("NOT FOUND")
else:
    print(res)
    for i in range(n):
        for j in range(m):
            if a[i][j] ==res:
                print("Vi tri ["+str(i)+"]["+str(j)+"]")
