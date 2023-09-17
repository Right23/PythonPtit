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
        nt = 0
        knt = 0
        for i in range(0, len(s), 1):
            if snt(int(s[i]))==1:
                nt += 1
            else:
                knt += 1
        # print(nt, knt)
        if nt<knt or snt(len(s))==0:
            print('NO')
        else:
            print('YES')
        t-=1
if __name__ == '__main__':
   solve()
    