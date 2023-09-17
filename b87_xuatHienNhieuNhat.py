for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    if len(a)==1:
        print(a[0])
    else:
        ans, m, res = a[0], {}, 1
        for i in a:
            if i in m:
                m[i]+=1
                if m[i] > res:
                    res, ans = m[i], i
            else:
                m[i] = 1
        if res*2 > len(a):
            print(ans)
        else:
            print("NO")