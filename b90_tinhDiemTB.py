n = int(input())
a = [float(i) for i in input().split()]
ma, mi = max(a), min(a)
c = []
for i in a:
    if i!=ma and i!=mi:
        c.append(i)
print('{:.2f}'.format(sum(c)/len(c)))