def solve(s):
    sum = 0
    res = []
    tmp=[i for i in s]
    for i in tmp:
        if i.isdigit():
            sum += int(i)
        else:
            res.append(i)
    res.sort()
    for i in res:
        print(i, end='')
    print(sum)
for t in range(int(input())):
    s = input()
    solve(s)

    

