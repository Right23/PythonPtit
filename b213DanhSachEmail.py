
f = open("CONTACT.in", "r")
my_set= set()
data = f.read().split('\n')
for i in range(len(data)):
    my_set.add(data[i].lower())
for i in sorted(my_set):
    print(i)
