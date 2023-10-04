from functools import cmp_to_key
class Student:
    def __init__(self, ma, name, total):
        self.ma = ma
        self.name = name
        self.avg = round(total/12+0.01 , 1)

    def getStatus(self):
        if self.avg>=9:
            return "XUAT SAC"
        elif self.avg>=8:
            return "GIOI"
        elif self.avg>=7:
            return "KHA"
        elif self.avg>=5:
            return "TB"
        else:
            return "YEU"
    
    def __str__(self):
        return '{} {} {} {}'.format(self.ma, self.name, self.avg, self.getStatus())

arr = []
for i in range(int(input())):
   ma = 'HS{:02}'.format(i+1)
   name = input()
   mark = [float(i) for i in input().split()]
   total = sum(mark)+mark[0]+mark[1]
   arr.append(Student(ma, name, total))
arr.sort(key=lambda x:(-x.avg, x.ma))
print(*arr, sep= '\n')