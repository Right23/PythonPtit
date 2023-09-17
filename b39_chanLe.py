from math import*

def solve():
    t = int(input())
    while(t>0):
       s = str(input())
       sum = 0
       ok = 1
       for i in range(0,len(s)-1, 1):
            if(abs(int(s[i])-int(s[i+1]))!=2):
                ok = 0
                break
       for i in range(0, len(s), 1):
            sum += int(s[i])
       if(sum%10==0 and ok ==1):
            print('YES')
       else:
            print('NO')
       t-=1
       
if __name__ == '__main__':
    solve()