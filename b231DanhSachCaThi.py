class ca:
    def __init__(self, id, date, time, code):
        self.id = id
        self.date = date
        self.time = time
        self.code = code
    def __str__(self):
        return '{} {} {} {}'.format(self.id, self.date, self.time, self.code)

f = open("CATHI.in", "r")
arr = []
for i in range(int(f.readline())):
    id = 'C{:03}'.format(i+1)
    date = str(f.readline().strip())
    time = str(f.readline().strip())
    code = str(f.readline().strip())
    arr.append(ca(id, date, time, code))
arr.sort(key=lambda x:(x.date, x.time, x.id))
for i in arr:
    print(i)



        