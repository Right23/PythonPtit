from math import*
def check(n):
    rev = 0
    tmp = n
    ok=1
    cnt=0
    while n != 0:
       if (n%10)%2==1:
           ok = 0
           break
       rev = rev*10 + n%10
       n//=10
       cnt+=1
       
    return rev==tmp and cnt%2==0

def solve():
    t = int(input())
    while(t>0):
        n = int(input())
        for i in range(20, n, 1):
            if check(i):
                print(i, end=' ')
        print()
        t-=1
if __name__ == '__main__':
    solve()

    