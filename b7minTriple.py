for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    res = 10**20
    for i in range(n-2):
        left = i+1
        right = n-1
        while left < right:
            tmp = a[i]+a[left]+a[right]
            