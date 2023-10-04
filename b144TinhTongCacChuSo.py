def solve(s):
    sum = 0
    ans=[i for i in s]
    for i in ans:
        if i.isdigit():
            sum+=int(i)
            ans.remove(i)
    ans.sort()
    for i in ans:
        if i != '0':
            print(i, end='')
    print(sum)
for t in range(int(input())):
    s = input()
    solve(s)

    

