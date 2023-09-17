for t in range(int(input())):
    n, id = map(int, input().split())
    a = list(i for i in input().split())
    # a = input().split()
    # print(a[id:], a[:id])
    print(*(a[id:] + a[:id]))