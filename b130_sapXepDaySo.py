for t in range(int(input())):
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    ma = max(a)
    id = a.index(ma)
    a.insert(id, m)
    
    for i in range(len(a)-1, -1, -1):
        if a[i] < 0:
            a.insert(0, a[i])
            a.remove(a[i])
    
