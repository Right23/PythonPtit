from math import*
def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)
#
def sieve():
    Max = int(1e6+1)
    prime = [1]*Max
    prime[0] = prime[1] = 0
    for i in range(2, 1000):
        if prime[i]:
            for j in range(i*i, Max, i):
                prime[j] = 0
                
def snt(x):
    if(x<2): return 0
    for i in range(2,isqrt(x)+1):
        if(x%i==0): return 0
    return 1
if __name__ == '__main__':
    t = int(input())
    while(t>0):
        cnt = 0
        n = int(input())
        for i in range(1, n+1):
            if(gcd(i, n)==1):
                cnt +=1
        if(snt(cnt)==1):
            print("YES\n")
        else:
            print('NO\n')
        t-=1