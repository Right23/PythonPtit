global n; x = []*100; used = []*100
def inkq():
    tmp = []
    for i in range(1, n+1):
        tmp.append(x[i])
    print(len(tmp))
    for i in tmp:
        print(i, end=' ')
    print()
def Try(i):
    for j in range(1, n+1):
        if not used[j]:
            x[i] = j
            used[j] = True
            if i == n:
                inkq()
            else:
                Try(i+1)
            used[j] = False
for t in range(int(input())):
    n = int(input())
    used = [False]*100
    Try(1)
    


