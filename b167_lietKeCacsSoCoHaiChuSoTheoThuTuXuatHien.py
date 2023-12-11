s = input()
se = set()
a = []
l = len(s) if len(s)%2==0 else len(s)-1
for i in range(0, l, 2):
    if s[i:i+2] not in se:
        a.append((s[i:i+2]))
        se.add(s[i:i+2])
print(*a)