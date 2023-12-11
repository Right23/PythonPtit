def count_0(n, k):
    cnt = 0
    tmp = str(bin(n)[2:])
    for i in tmp:
        if i == '0':
            cnt+=1
    if cnt == k:
        return True
    return False
for t in range(int(input())):
    n, k = map(int, input().split())
    cnt = 0
    for i in range(0, n+1):
        if count_0(i, k):
            cnt+=1
            print(bin(i))
    print(cnt)
    