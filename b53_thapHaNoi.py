from math import*
def chuyen(n, a, b, c):
    if n==1:
        print(chr(a+64), '->', chr(c+64), sep=' ')
    else:
        chuyen(n-1, a, c, b)
        chuyen(1, a, b, c)
        chuyen(n-1, b, a, c)

if __name__ == '__main__':
    n = int(input())
    chuyen(n, 1, 2, 3)
    