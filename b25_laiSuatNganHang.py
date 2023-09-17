from math import*
def check():
    t = int(input())
    while(t>0):
        n, x, m = map(float, input().split())
        res = 0
        for i in range(1, 100000):
            if(n*(1+x/100)**i) >= m:
                res = i
                break
        print(res)
        t-=1
if __name__ == '__main__':
    check()