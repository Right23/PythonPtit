    # co the dung set
for t in range(int(input())):
    n = int(input())
    cnt = [0]*1001
    a = []
    for i in range(n):
        x = int(input())
        if x in a:
            cnt[x]+=1
        else:
            cnt[x] = 1
        a.append(x)
    res = max(cnt)
    # 
    # sorted(a)
    a.sort()
    # for i in a:
    #     print(i, end=' ')
    for i in a:
        if cnt[i]==res:
            print(i)
            break


