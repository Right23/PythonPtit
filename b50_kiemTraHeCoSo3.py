def solve():
    t = int(input())
    while(t>0):
        s = str(input())
        ok = 1
        for x in s:
            if x!='0' and x!='1' and x!='2':
                ok = 0
                break
        if ok == 1:
            print('YES') 
        else:
            print('NO')
        
        t-=1
if __name__ == '__main__':
    solve()
