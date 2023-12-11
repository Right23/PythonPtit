def dec_to_baseN(decimal, base):
    res = ""
    baseN_digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while decimal>0:
        remainder = decimal%base
        res = baseN_digits[remainder]+res
        decimal//=base
    return res

for t in range(int(input())):
    n, b = map(int, input().split())
    # n = int(input())
    # b = int(input())
    print(dec_to_baseN(n, b))
