class SV:
    def __init__(self, id, name, unit, atd):
        # atd = attendance
        self.id = id
        self.name = name
        self.unit = unit
        self.atd = atd
    def get_mark_atd(self):
        res = 10
        for i in self.atd:
            if i == 'v':
                res -= 2
            elif i == 'm':
                res -= 1
        if res < 0:
            res = 0
        return res
    def check_condition(self):
        if self.get_mark_atd() == 0:
            return "KDDK"
        return ""
    def __str__(self):
        return '{} {} {} {} {}'.format(self.id, self.name, self.unit, self.get_mark_atd(), self.check_condition())
arr = []
n = int(input().strip())
tmp = []
for i in range(n):
    id = input().strip()
    name = input().strip()
    unit = input().strip()
    temp = [id, name, unit]
    tmp.append(temp)
for i in range(n):
    id, atd = input().strip().split()
    for i in range(n):
        if id == tmp[i][0]:
            tmp[i].append(atd)
            break
for i in tmp:
    id, name, unit, atd = i[0], i[1], i[2], i[3]
    arr.append(SV(id, name, unit, atd))
for i in arr:
    print(i)




