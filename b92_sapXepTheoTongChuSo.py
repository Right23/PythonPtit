def sumDigit(n):
    res = 0
    for i in n:
        res+=int(i)
    return res

for t in range(int(input())):
    n = int(input())
    a = input().split()
    # a.sort(key = lambda x: (sum(int(i) for i in x), int(x)))
    a.sort(key= lambda x :(sumDigit(x), int(x)))
    print(*a)