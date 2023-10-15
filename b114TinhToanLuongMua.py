class Pos:
    def __init__(self, id, name, time, luongmua):
        self.id = id
        self.name = name
        self.time = time
        self.luongmua = luongmua
        self.avg = round((self.luongmua/self.time)*60, 2)
    def __str__(self):
        return '{} {} {:.2f}'.format(self.id, self.name, self.avg)

def sum_time(st, en):
    time1 = int(st[0:2])*60 + int(st[3:])
    time2 = int(en[0:2])*60 + int(en[3:])
    return time2 - time1

arr = []
ten = []
# ten de luu ten cac tram
for i in range(int(input().strip())):
    id = 'T{:02}'.format(i+1)
    name = input().strip()
    st = input().strip()
    en = input().strip()
    luongmua = int(input().strip())
    time = sum_time(st, en)
    if name not in ten:
        arr.append(Pos(id, name, time, luongmua))
        ten.append(name)
    else:
        for j in arr:
            if name == j.name:
                id = j.id
                time += j.time
                luongmua += j.luongmua
                arr.remove(j)
                arr.append(Pos(id, name, time, luongmua))
                break
arr.sort(key=lambda x: x.id)
for i in arr:
    print(i)
    
    