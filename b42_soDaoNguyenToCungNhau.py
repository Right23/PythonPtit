from math import*
def soDao(n):
    rev = 0
    tmp = n
    while n != 0:
       rev = rev*10 + n%10
       n//=10
    return rev
def gcd(a, b):
    if b==0: 
        return a
    return gcd(b, a%b)
def solve():
    t = int(input())
    while(t>0):
        n = int(input())
        if(gcd(n, soDao(n)) == 1):
            print("YES")
        else:
            print("NO")
        t-=1
if __name__ == '__main__':
    solve()

    