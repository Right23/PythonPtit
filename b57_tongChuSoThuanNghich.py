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
        tmp = n
        sum = 0
        while n != 0:
            sum+=n%10
            n//=10
        if sum>9 and sum==soDao(sum):
            print('YES')
        else:
            print('NO')
        t-=1
if __name__ == '__main__':
    solve()