n, m = map(int,input().split())
a=[[0]]*n
Ma, Mi, ok, da_In = 0, 10**6, 0, 0
# da_In de kiem tra xem da in khoang cach hay chua
for i in range(n):
    a[i] = [int(i) for i in input().split()]
    Ma = max(Ma, max(a[i]))
    Mi = min(Mi, min(a[i]))
for i in range(n):
    for j in range(m):
        if a[i][j]==Ma-Mi:
            if da_In==0:
                print(Ma-Mi)
                da_In = 1
                ok = 1
            print("Vi tri [", i, "]", "[", j, "]", sep='')
if ok==0:
    print("NOT FOUND")
