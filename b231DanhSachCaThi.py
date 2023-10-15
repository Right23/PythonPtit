class ca:
    def __init__(self, id, date, time, code):
        self.id = id
        self.date = date
        self.time = time
        self.code = code
    def __str__(self):
        return '{} {} {} {}'.format(self.id, self.date, self.time, self.code)

f = open("CATHI.in", "r")
tmp = [i for i in f.read().split()]
arr = []
j = 1
t = tmp[0]
for i in range(1, len(tmp), 3):
    id = 'C{:03}'.format(j)
    j+=1
    date = tmp[i]
    time = tmp[i+1]
    code = tmp[i+2]
    arr.append(ca(id, date, time, code))
arr.sort(key=lambda x: (x.date, x.time, x.id))
for i in arr:
    print(i)
# for i in tmp:
#     print(i)


        