for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    L , R = min(a), max(a)
    cnt = 0
    for i in range(L, R+1):
        if i not in a:
            cnt+=1
    print(cnt)
    