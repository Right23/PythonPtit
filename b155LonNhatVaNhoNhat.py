while True:
    n = int(input())
    if n==0:
        break
    a=[]
    for i in range(n):
        k = int(input())
        a.append(k)
    a.sort()
    if a[0]==a[len(a)-1]:
        print("BANGNHAU")
    else:
        print(a[0], a[len(a)-1], sep=' ')