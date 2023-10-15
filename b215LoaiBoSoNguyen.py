f = open("DATA.in", "r")
a = [i for i in f.read().split()]
b = []
for i in a:
    try:
        n = int(i)
        if n <= -2147483648 or n >= 2147483647:
            b.append(str(n))
    except Exception:
        b.append(i)
c = sorted(b)
for i in c:
    print(i, end=' ')