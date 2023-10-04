class NV:
    def __init__(self, id, name, lt, th):
        self.id = id
        self.name = name
        if lt > 10:
            self.lt = lt/10
        else:
            self.lt =lt
        if th > 10:
            self.th = th/10
        else:
            self.th = th
        self.avg = (self.lt+self.th)/2
    def get_Status(self):
        if self.avg > 9.5:
            return "XUAT SAC"
        elif self.avg >= 8:
            return "DAT"
        elif self.avg >= 5:
            return "CAN NHAC"
        return "TRUOT"
    def __str__(self): 
        return self.id+" "+self.name+" "+'{:.2f}'.format(self.avg)+" "+self.get_Status() 
    
arr = []
for i in range(int(input())):
    id = 'TS0{}'.format(i+1)
    name = input()
    lt = float(input())
    th = float(input())
    nv = NV(id, name, lt, th)
    arr.append(nv)
arr.sort(key=lambda x: -x.avg)
for i in arr:
    print(i)