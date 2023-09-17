from math import*
def check(x):
    ok = 1
    while(x>0):
        if(x%10 !=4 and x%10 !=7):
            ok=0
            break
        x//=10
    if ok == 1:
        print('YES')
    else:
        print("NO")
if __name__ == '__main__':
    t = int(input())
    while(t>0):
        n = int(input())
        check(n)
        t-=1