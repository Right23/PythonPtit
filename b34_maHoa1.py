from math import*
def solve():
    t = int(input())
    while(t>0):
        s = str(input())
        cnt = 1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                cnt+=1
            else:
                print(cnt,s[i], sep='', end='')
                cnt=1
        print(cnt, s[len(s)-1],sep='', end='')
        t-=1
        print()
if __name__ == '__main__':
    solve()
            