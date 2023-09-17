from math import*


def solve():
    t = int(input())
    while(t>0):
        n = int(input())
        if n%3==0:
            print('YES')
        else:
            print('NO')
        t-=1
if __name__ == '__main__':
    solve()