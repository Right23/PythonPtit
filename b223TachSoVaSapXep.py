arr = []
for t in range(int(input())):
    s = input()
    tmp = 0
    for i in range(len(s)):
        if s[i].isdigit():
            tmp*=10+int(s[i])
        else:
            if tmp != 0:
                arr.append(tmp)
                tmp = 0
for i in (arr):
    print(i)