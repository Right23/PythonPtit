def solve():
    t = int(input())
    while(t>0):
        s = str(input())
        ok = 1
        if len(s)<3:
            ok = 0
        pivot = 0# chot
        for i in range(0, len(s)-1, 1):
            if s[i]>s[i+1]:
                pivot = i
                break
            elif s[i]==s[i+1]:
                break
        for i in range(pivot, len(s)-1, 1):
            if(s[i]<=s[i+1]):
                ok = 0
                break
        if (pivot!=0 and pivot!=len(s)-1 and ok==1):
            print('YES')
        else:
            print('NO')
        
        t-=1
if __name__ == '__main__':
    solve()
