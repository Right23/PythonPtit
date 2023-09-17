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
        n = int(input())
        tmp = n
        sum = 0
        while n != 0:
            sum+=n%10
            n//=10
        if snt(sum):
            print('YES')
        else:
            print('NO')
        t-=1
if __name__ == '__main__':
    solve()