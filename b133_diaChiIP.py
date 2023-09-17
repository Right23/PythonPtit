def check(n):
    a = [int(i) for i in n.split('.')]
    for i in a:
        if i < 0 or i> 255:
            return "NO"
    return "YES"

for t in range(int(input())):
    a = [int(i) for i in input().split('.')]
    ok = "YES"
    for i in a:
        if i <0 or i >255:
            ok = "NO"
            break
    # for i in a:
    #     print(type(i), sep=' ', end=' ')
    print(ok)
   