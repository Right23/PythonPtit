from math import*
def snt(n):
    if n < 2: 
        return 0
    for i in range(2, int(sqrt(n))+1, 1):
        if n%i==0:
            return 0
    return 1

for t in range(int(input())):
    s = (input())
    le, cnt = len(s), 0
    for i in s:
        if snt(int(i)):
            cnt+=1
    if snt(len(s)) and cnt>le-cnt:
        print("YES")
    else:
        print('NO')