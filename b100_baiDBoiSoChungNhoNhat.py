from math import*
# elpulga
def count(a, b):
    res = 0
    lcm = 1
    for i in range(a, b+1):
        lcm*=i
    for x in range(1, lcm+1):
        for y in range(1, lcm+1):
            if lcm == x*y//gcd(x, y):
                res+=1
                # print(x, y, sep=' ')
    # print(res)
    return res
for t in range(int(input())):
    a, b = map(int, input().split())
    # count(a, b)
    print(count(a, b))
