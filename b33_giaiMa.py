def solve():
    t = int(input())
    while(t>0):
        s = str(input())
        for i in range(0, len(s), 2):
            print(int(s[i+1])*s[i], end='')
        print()
        t-=1
if __name__ == '__main__':
    solve()