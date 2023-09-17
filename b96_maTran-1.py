n = int(input())
a=[[]]*n
for i in range(n):
    a[i] = [int(j) for j in input().split()]
s_up, s_do = 0, 0
for i in range(n):
    for j in range(n):
        if i < j:
            s_up += a[i][j]
        elif i > j:
            s_do += a[i][j]
k = int(input())
dif = abs(s_up-s_do)
if dif > k:
    print("NO")
else:
    print("YES")
print(dif)

