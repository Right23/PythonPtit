from math import*
def snt(n):
    if n < 2: 
        return 0
    for i in range(2, int(sqrt(n))+1, 1):
        if n%i==0:
            return 0
    return 1
for t in range(int(input())):
    s = input()
    if snt(int(s[:3]))==1 and snt(int(s[-3:]))==1:
        print("YES")
    else:
        print("NO")