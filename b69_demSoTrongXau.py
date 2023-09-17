for t in range(int(input())):
    s = input()
    k = input()
    cnt = 0

    i = s.find(k)
    while i!=-1:
        cnt+=1
        # tim trong doan tu i+1 ve sau
        i = s.find(k, i + len(k))
    print(cnt)