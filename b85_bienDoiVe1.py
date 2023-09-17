while True:
    n = int(input())
    if n==0:
        break
    cnt = 0
    a = {n}
    while n!=1:
        if n%2==1:
            n = n*3+1
            a.add(n)
        else:
            n = n//2
            a.add(n)
    print(len(a))        

