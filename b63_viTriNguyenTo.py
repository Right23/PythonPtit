from math import*

def snt(x):
    if x<2:
        return 0
    for i in range(2, isqrt(x)+1, 1):
        if x%i==0:
            return 0
    return 1

def solve():
    t = int(input())
    while(t>0):
        s = str(input())
        ok = 1
        for i in range(0, len(s), 1):
            if snt(i) and snt(int(s[i]))==0:
                ok = 0
                break
            if snt(i)==0 and snt(int(s[i])):
                ok = 0
                break

        if ok == 1:
            print('YES') 
        else:
            print('NO')
        t-=1
if __name__ == '__main__':
    solve()