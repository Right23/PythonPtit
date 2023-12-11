n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
s1, s2 = '', ''
for x in a:
    s1+=str(x)
for x in b:
    s2+=str(x)
if s1 == s2:
    print('YES')
else:
    print('NO')
