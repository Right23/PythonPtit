class SV :
    def __init__(self, ma, ten, team, tr) :
        self.ma = 'C{:03d}'.format(ma)
        self.ten = ten
        self.team = team
        self.tr = tr
        
    def __str__(self):
        return '{} {} {} {}'.format(self.ma, self.ten, self.team, self.tr)
t = [0]
# team khoi tao la team 0
for i in range(int(input())):
    t.append([input(), input()])
arr = []
for i in range(int(input())):
    name = input()
    team = input()
    arr.append(SV(i+1, name, t[int(team[4::])][0], t[int(team[4::])][1]))
arr.sort(key=lambda x: x.ten)
for i in arr:
    print(i)