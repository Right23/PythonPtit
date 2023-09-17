import math

Max = int(1e6+1)
prime = [1]*Max
prime[0] = prime[1] = 0
for i in range(1000):
    if prime[i]:
        for j in range(i*i, Max, i):
            prime[j] = 0 
# 
def snt(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True  

p = [0, 2]          
k = 3
while len(p) <= 1001:
    if prime[k]:
        p.append(k)
        # p += [k]
    k+=2
n, x = [int(i) for i in input().split()]
for i in range(n+1):
    x += p[i]
    print(x, end=' ')