class sv:
    def __init__(self, id, name, unit):
        self.id = id
        self.name = name
        self.unit = unit
        self.atd = ''
    def set_atd(self, attendance):
        self.atd = attendance
    def get_mark_atd(self):
        res = 10
        for x in self.atd:
            if x=='v':
                res-=2
            elif x=='m':
                res-=1
        if res < 0:
            res = 0
        return res
    def get_condition(self):
        if self.get_mark_atd()==0:
            return 'KDDK'
        return ''
    def __str__(self) -> str:
        return '{} {} {} {} {}'.format(self.id, self.name, self.unit, self.get_mark_atd(), self.get_condition())
arr = []
n = int(input())
for i in range(n):
    id = input().strip()
    name = input().strip()
    unit = input().strip()
    arr.append(sv(id, name, unit))
for i in range(n):
    id, atd = input().strip().split()
    for j in arr:
        if j.id == id:
            j.set_atd(atd)
            break
for i in arr:
    print(i)