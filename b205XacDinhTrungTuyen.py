class TS:
    def __init__(self, id, name, code, i_mark, s_mark):
        self.id = id
        self.name = name
        self.code = code
        self.i_mark = i_mark
        self.s_mark = s_mark
    def subject(self):
        if self.code[0]=="A":
            return "TOAN"
        elif self.code[0]=="B":
            return "LY"
        return "HOA"
    def get_sum(self):
        sum = 0
        if self.code[1]=="1":
            sum+=2.0
        elif self.code[1]=="2":
            sum+=1.5
        elif self.code[1]=="3":
            sum+=1.0
        sum += self.i_mark*2 + self.s_mark
        return sum
    def status(self):
        if self.get_sum() >= 18:
            return "TRUNG TUYEN"
        return "LOAI"
    def __str__(self):
        return '{} {} {} {:.1f} {}'.format(self.id, self.name, self.subject(), self.get_sum(), self.status())
a = []
for i in range(int(input().strip())):
    id = 'GV{:02}'.format(i+1)
    name = input().strip()
    code = input().strip()
    i_mark = float(input().strip())
    s_mark = float(input().strip())
    ts = TS(id, name, code, i_mark, s_mark)
    a.append(ts)
a.sort(key=lambda x: -x.get_sum())
for i in a:
    print(i)
    
