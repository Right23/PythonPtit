from math import*
def solve():
    t = int(input())
    while(t>0):
        n = int(input())
        print('1 * ', end='')
        for i in range(2, n+1, 1):
            mu = 0
            while(n%i==0):
                mu+=1
                n//=i
            if mu!=0:
                print(i,'^',mu, sep='', end='')
                if(n>1):
                    print(' * ', end='')
        print()
        t-=1
if __name__ == '__main__':
    solve()
