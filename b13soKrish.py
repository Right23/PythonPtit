import math
def Krish(n):
    tmp = n
    tong = 0
    while n!=0:
        tong += math.factorial(n%10)
        n//=10
    return tmp == tong
for t in range(int(input())):
    n = int(input())
    if Krish(n):
        print("Yes")
    else:
        print("No")
    
