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
        sum = 0
        for i in range(0, len(s), 1):
            sum += int(s[i])
            if i%2==0 and int(s[i])%2==1:
                ok = 0
                break
            if i%2==1 and int(s[i])%2==0:
                ok = 0
                break
        if ok == 1 and snt(sum):
            print("YES")
        else:
            print("NO")
        t-=1
if __name__ == '__main__':
    solve()