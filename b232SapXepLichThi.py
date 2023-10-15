class subject:
    def __init__(self, date, time, id_room, name, gr, amount, macathi):
        self.date = date
        self.time=time
        self.id_room=id_room
        self.name=name
        self.gr=gr
        self.amount=amount
        self.macathi = macathi
    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.date, self.time, self.id_room, self.name, self.gr, self.amount)

m = open("MONTHI.in", "r")
c = open("CATHI.in", "r")
l = open("LICHTHI.in", "r")
ma = [i for i in m.read().split('\n')]
ca = [i for i in c.read().split()]
la = [i for i in l.read().split()]

date = []
time = []
id_room = []
name = []
gr = []
amount = []
macathi = []
n = int(ma[0])
# lay du lieu
for j in range(1, len(ma), 3):
    name.append(ma[j+1])
for j in range(1,len(ca), 3):
    date.append(ca[j])
    time.append(ca[j+1])
    id_room.append(ca[j+2])
for j in range(1, len(la), 4):
    macathi.append(la[j])
    gr.append(la[j + 2])
    amount.append(la[j+3])

arr = []
for i in range(n):
    arr.append(subject(date[i], time[i], id_room[i], name[i], gr[i], amount[i], macathi[i]))
arr.sort(key=lambda x: (x.date, x.time, x.macathi))
for i in arr:
    print(i)
