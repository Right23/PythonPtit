for t in range(int(input())):
    res = ""
    s = input().split()
    for i in s:
        if len(res + i + " ") <= 100:
            res += i + " "
        else:
            break
    print(res)
    