from math import floor


if __name__=='__main__':
    t = int(input())
    while t>0:
        n, m, L = map(int, input().split())
        h = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            h[i] = list(map(int, input().split()))
        k = [[1 for _ in range(L)] for _ in range(L)]
        
        res = [[0 for _ in range(m-2)] for _ in range(n-2)]
        ans = 0
        for i in range(n-2):
            for j in range(m-2):
                for p in range(L):
                    for q in range(L):
                        res[i][j] += h[i+p][j+q]*k[p][q]
                res[i][j] = floor(res[i][j] / (L*L))
                # ans += res[i][j]
        # print(ans)
        # print(res)
        for i in range(n-2):
            for j in range(m-2):
                print(res[i][j], end=' ')
            print()
        t-=1
        
