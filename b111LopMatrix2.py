for t in range(int(input())):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append([int(j) for j in input().split()])
    b = []*m
    for i in range(m):
        b.append([0]*n)
    for i in range(n):
        for j in range(m):
            b[j][i] = a[i][j]
    c = []*n
    for i in range(n):
        c.append([0]*n)
    for i in range(n):
        for j in range(n):
            c[i][j] = 0
            for k in range(m):
                c[i][j] += a[i][k]*b[k][j]
    for i in c:
        print(*i)
    
