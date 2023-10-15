def tn(s):
    tmp = s[::-1]
    return s==tmp
f = open("VANBAN.in", "r")
a = f.read()
tmp = ""
res = -1
ans = ""
b = []
for i in range(len(a)):
    if a[i] != ' ' and a[i] != '\n':
        tmp += a[i]
    else:
        if tn(tmp):
            res = max(len(tmp), res)
            ans = tmp
            tmp = ""
            b.append(ans)
if tn(tmp):
    res = max(len(tmp), res)
    if len(tmp) >= res:
        b.append(tmp)

for i in b:
    if len(i) == res:
        print(i, res, sep=' ')



        