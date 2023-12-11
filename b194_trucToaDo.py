t = int(input())
while t>0:
    n = int(input())
    a = []
    for _ in range(n):
        x, y = map(int, input().split())
        a.append((x, y))
    a.sort(key=lambda x: x[1])
    cnt, endPoint = 1, a[0][1]

    for i in range(1, n):
        if a[i][0] >= endPoint:
            endPoint = a[i][1]
            cnt+=1
    print(cnt)
    t-=1
