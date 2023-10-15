from math import *
mod = int(1e9)+7
def binpow(a, b):
    if b==0:
        return 1
    if b==1:
        return a%mod
    x = binpow(a, b//2)
    if b%2==0:
        return (x*x)%mod
    return((x*x%mod)*a)%mod
for t in range(int(input())):
    n, k = map(int, input().split())
    sum = 0
    for i in range(1, n+1):
        sum += binpow(i, k)
        sum %= mod
    print(sum)