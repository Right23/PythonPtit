from math import*
def snt(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x))+1, 1):
        if x % i == 0:
            return False
    return True

if __name__=='__main__':
    n = int(input())
    a = []
    while len(a) < n:
        a.extend(list(map(int, input().split())))
    is_nt = sorted([x for x in a if snt(x)])
    isnot_snt = [x for x in a if not snt(x)]
    i1, i2 = 0, 0
    for x in a:
        if snt(x):
            print(is_nt[i1], end=' ')
            i1+=1
        else:
            print(isnot_snt[i2], end=' ')
            i2+=1
    