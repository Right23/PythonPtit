from math import*
def soDao(n):
    rev = 0
    tmp = n
    while n != 0:
       rev = rev*10 + n%10
       n//=10
    return rev
def solve():
    t = int(input())
    while(t>0):
        n = int(input())
        ok = 0
        if n%7 == 0:
            ok = 1
        else:
            for i in range(1, 1001, 1):
                tmp = n + soDao(n)
                if tmp%7==0:
                    n = tmp
                    ok = 1
                    break
                else:
                    n = tmp
        if ok == 0:
            print(-1)
        else:
            print(n)
        t-=1
if __name__ == '__main__':
    solve()
