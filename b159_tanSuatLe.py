t = int(input())
while t>0:
    n = int(input())
    a = [int(x) for x in input().split()]
    # for x in a:
    #     if a.count(x)%2==1:
    #         print(x)
    #         break
    c = [0]*100001
    for x in a:
        c[x]+=1
    for x in a:
        if c[x]%2==1:
            print(x)
            break
    t-=1
    