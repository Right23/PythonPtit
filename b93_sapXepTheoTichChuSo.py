def mul(s):
    x = 1
    for i in s:
        x *= int(i)
    return x

def sumDigit(n):
    res = 0
    for i in n:
        res+=int(i)
    return res

for t in range(int(input())):
    n = int(input())
    a = input().split()
    a.sort(key=lambda s: (mul(s), int(s)))
    print(*a)