Max = int(1e6+1)
prime = [1]*Max
prime[0] = prime[1] = 0
for i in range(1000):
    if prime[i]:
        for j in range(i*i, Max, i):
            prime[j] = 0    
def soDao(n):
    rev = 0
    # tmp = n
    while(n!=0):
        rev = rev*10 + n%10
        n//=10
    return rev
for t in range(int(input())):
    c = [0]*Max
    n=int(input())
    for i in range(n):
        if (i!=soDao(i)) and (prime[i]==prime[soDao(i)]==1) and soDao(i)< n:
            if c[i] == 0:
                print(i, soDao(i), end=' ')
                c[i] = c[soDao(i)] = 1
    print()
            