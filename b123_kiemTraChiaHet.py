def count(L, R, N):
    cnt = 0
    primes = sieve_of_eratosthenes(N)
    for num in range(L, R+1):
        divisible = False
        for prime in primes:
            if num%prime==0:
                divisible = True
                break
        if divisible==False:
            cnt+=1
    return cnt
def sieve_of_eratosthenes(N):
    primes = [True]*(N+1)
    primes[0]= primes[1] = False
    p = 2
    while p*p <= N:
        if primes[p]:
            for i in range(p*p, N+1, p):
                primes[i] = False
        p+=1
    #  mang chua cac so nguyen to nho hon N
    prime_list = []
    for i in range(2, N+1):
        if primes[i]:
            prime_list.append(i)
    return prime_list

while True:
    # inputs = input().split()
    # if len(inputs)==1 and inputs[0]==-1:
    #     break
    inputs = input()
    if inputs=="-1":
        break
    L, R = map(int, inputs.split())
    N = int(input())
    print(count(L, R, N))
    
    
