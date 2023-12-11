# s = input()
# se = []
# a = []
# l = len(s) if len(s)%2==0 else len(s)-1
# for i in range(0, l, 2):
#     if s[i:i+2] not in se:
#         a.append((s[i:i+2]))
#     se.append((s[i:i+2]))
# for x in a:
#     print(x, se.count(x), sep=' ')
s = input()
d = dict()
for i in range(0, len(s)-1, 2):
    tmp = s[i:i+2]
    if tmp in d:
        d[tmp]+=1
    else:
        d[tmp]=1
for x in d:
    print(x, d[x])
for key, value in d.items():
    print(key, value, sep=' ')