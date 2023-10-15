def tn(s):
    tmp = s[::-1]
    return s==tmp
f = open("VANBAN.in", "r")
a = [i for i in f.read().split()]
res = -1
ans = ""
b = []
dain = {}
for i in a:
    if tn(i):
        if len(i) >= res:
            res = len(i)
            ans = i
            b.append(ans)
for i in b:
    dain[i] = False
for i in b:
    if len(i) == res and dain[i] == False:
        print(i, a.count(i), sep=' ')
        dain[i] = True
            