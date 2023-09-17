a = []
for t in range(int(input())):
    b = []
    name = str(input())
    score, sub = map(int, input().split())
    b.append(name)
    b.append(score)
    b.append(sub)
    a.append(b)
a.sort(key=lambda x: (-x[1], x[2], x[0]))
for x in a:
    for i in x:
        print(i, end=' ')
    print()
