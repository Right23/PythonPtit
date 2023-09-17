from math import*


def solve():
    t = int(input())
    while(t>0):
        s = str(input())
        ok = 1
        if len(s)%2==0 or s[0]==s[1]:
            ok = 0
        for i in range(2, len(s), 2):
            if s[i]!=s[0]:
                ok = 0
                break
        if ok == 1:
            print("YES")
        else:
            print("NO")
        t-=1
if __name__ == '__main__':
    solve()