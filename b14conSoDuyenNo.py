for t in range(int(input())):
    a = list(int(i) for i in input())
    if a[:1]==a[len(a)-1:]:
        print("YES")
    else:
        print("NO")