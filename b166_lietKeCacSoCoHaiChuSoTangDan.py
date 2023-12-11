s = input()
se = set()
l = len(s) if len(s)%2==0 else len(s)-1
for i in range(0, l, 2):
    se.add(s[i:i+2])
print(*sorted(se))
