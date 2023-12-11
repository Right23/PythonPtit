se1, se2 = set(), set()
f = open('DATA1.in')
while True:
    line = f.readline()
    if not line:
        break
    for x in line.split():
        se1.add(x.lower())

f = open('DATA2.in')
while True:
    line = f.readline()
    if not line:
        break
    for x in line.split():
        se2.add(x.lower())
for x in sorted(se1):
    if x not in se2:
        print(x, end=' ')
print()
for x in sorted(se2):
    if x not in se1:
        print(x, end=' ')
        