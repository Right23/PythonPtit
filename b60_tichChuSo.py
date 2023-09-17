from math import*


def solve():
    t = int(input())
    while(t>0):
        n = int(input())
        tich = 1
        while n!=0:
            if n%10 != 0:
                tich*=n%10
            n//=10
        print(tich)
        t-=1
if __name__ == '__main__':
    solve()