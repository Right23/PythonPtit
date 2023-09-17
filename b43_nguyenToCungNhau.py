from math import*

def gcd(a, b):
    if b==0: 
        return a
    return gcd(b, a%b)
def solve():
    cnt = 0
    n, k = map(int, input().split())
    for i in range(10**(k-1), 10**k, 1):
        if(gcd(n, i) == 1):
            cnt+=1
            print(i, end=' ')
            if(cnt%10==0):
                print()

if __name__ == '__main__':
    solve()

    