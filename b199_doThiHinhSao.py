n = int(input())
a = []
for i in range(n+1):
    a.append([])
for i in range(n-1):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)
check = False
for i in range(1, n+1):
    if len(a[i])==n-1:
        check = True
        break
print('Yes' if check==True else 'No')