from functools import cmp_to_key
class Student:
    def __init__(self, ma, name, diem):
        self.ma = str(ma)
        while len(self.ma) < 2:
            self.ma = '0'+self.ma
        self.ma = 'HS'+self.ma
        self.name = name
        self.diem = diem
    def getTong(self):
        return (0.01+sum(self.diem) + self.diem[0]+self.diem[1])/(len(self.diem)+2)
    def getStatus(self):
        if self.getTong()>=9:
            return "XUAT SAC"
        elif self.getTong()>=8:
            return "GIOI"
        elif self.getTong()>=7:
            return "KHA"
        elif self.getTong()>=5:
            return "TB"
        else:
            return "YEU"
    def getMa(self):
        return self.ma
    def __str__(self):
        return self.ma+' '+self.name+' '+'{:.1f}'.format(self.getTong().__round__(2))+' '+self.getStatus()
def cmp(a, b):
    if a.getTong()!=b.getTong():
        return b.getTong()-a.getTong()
    else:
        if a.getMa()<b.getMa():
            return -1
        else:
            return 1


if __name__ == '__main__':
    arr = []
    n = int(input())
    for i in range(n):
        std = Student(i+1, input(), [float(i) for i in input().split()])
        arr.append(std)
    arr.sort(key= lambda x: (-x.getTong(), x.getMa()))
    # arr.sort(key=cmp_to_key(cmp))
    for i in arr:
        print(i)

    
