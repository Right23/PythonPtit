n = input()
if abs(int(n)) <= 10:
    print(1)
else:
    cnt = 0
    while abs(int(n)) > 10:
        tmp = 0
        if n[0] == '-':
            for i in range(2, len(n)):
                tmp += int(n[i])
            tmp -= int(n[1])
        else:
            for i in range(len(n)):
                tmp += int(n[i])
        cnt += 1
        n = str(tmp)
    print(cnt)

