f = open("DATA.in", "r")
# a = [i for i in f.read().split()]
a = f.read().split()
b = []
for i in a:
    try:
        n = int(i)
        if n <= -1e10 or n >= 1e10:
            b.append(str(n))
    except Exception:
        b.append(i)
for i in sorted(b):
    print(i, end=' ')