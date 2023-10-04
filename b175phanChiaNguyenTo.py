from math import*
def isPrime(n):
    if n< 2:
        return 0
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
n = int(input())
a = [int(i) for i in input().split()]
b = {}
for x in a:
    b[x] = 1
a = list(b)
n = len(a)
for i in range(1, n):
    a[i] += a[i-1]
ok = 0
for i in range(n):
    if isPrime(a[i]) and isPrime(a[n-1]-a[i]):
        ok = 1
        print(i)
        break
if not ok:
    print("NOT FOUND")