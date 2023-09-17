import math


def snt(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True
def check(str):
    for i in str:
        if not snt(int(i)):
            return "No"
    tongChuSo = sum([int(i) for i in str])
    num1, num2 = str, str[::-1]
    if not snt(int(num1)) and not snt(int(num2)) and not snt(tongChuSo):
        return "No"
    return "Yes"
for t in range(int(input())):
    print(check(input()))