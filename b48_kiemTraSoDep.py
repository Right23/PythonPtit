def solve():
    t = int(input())
    while(t>0):
        s = str(input())
        ok = 1
        if s[0] == s[1]:
            ok = 0
        else:
            for i in range(2, len(s), 1):
                if (i%2==0 and int(s[i])!=int(s[0])) or (i%2==1 and int(s[i])!=int(s[1])):
                    ok = 0
                    break
        if ok == 1:
            print("YES")
        else:
            print("NO")
        t-=1
if __name__ == '__main__':
    solve()
