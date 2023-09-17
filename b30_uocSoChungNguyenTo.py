from math import*
def snt(x):
    if x < 2:
        return 0
    for i in range(2, isqrt(x)+1):
        if x%i==0:
            return 0
    return 1
def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)
def tongChuSo(x):
    sum = 0
    while(x>0):
        sum+=x%10
        x//=10
    return sum
def check():
    t = int(input())
    while(t>0):
        a, b= map(int, input().split())

        if(snt(tongChuSo(gcd(a, b)))):
            print("YES")
        else:
            print("NO")
        # print(gcd(a, b), tongChuSo(gcd(a, b)))
        t-=1
if __name__ == '__main__':
    check()