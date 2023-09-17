import itertools
def solve():
    t = int(input())
    while(t>0):
        s = str(input())
        b = len(s)-2
        e = len(s)
        # res = ''.join(itertools.islice(s, b, e))
        # print(''.join(itertools.islice(s, b, e)))
        res = s[b:e:1]
        if(res=='86'):
            print("YES")
        else:
            print("NO")
        # print(s[b:e:1])
        t-=1
if __name__ == '__main__':
    solve()