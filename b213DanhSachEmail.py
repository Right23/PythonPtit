
f = open("CONTACT.in", "r")
my_set = set()
data = f.read()
tmp = ""
for i in range(len(data)):
    if data[i] != '\n':
        tmp += data[i]
    else:
        my_set.add(tmp.lower())
        tmp = ""
my_set.add(tmp.lower())

for i in sorted(my_set):
    print(i)