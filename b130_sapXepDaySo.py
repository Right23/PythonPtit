for t in range(int(input())):
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    ma = max(a)
    id = a.index(ma)
    a.insert(id, m)
    
    for x in a:
        if x < 0:
            print(x, end=' ')
    for x in a:
        if x >= 0:
            print(x, end=' ')
    print()
    
