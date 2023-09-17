t = int(input())
for i in range(t):
    s = (input())
    s+='z'
    res = -10**10
    sum = 0
    # print(s)
    for i in range(len(s)):
        if s[i].isalpha():
            # if s[i-1].isdigit() and i>0:
            #     res = max(res, sum)
            res = max(res, sum)
            sum = 0
        else:
            sum = sum*10+int(s[i])
    print(res)
