from datetime import datetime

class GMer:
    def __init__(self, id, name, st, en):
        self.id = id
        self.name = name
        self.st = st
        self.en = en
        self.time = self.getTime()
    def getTime(self):
        bd = int(self.st[0:2])*60 + int(self.st[3:])
        kt = int(self.en[0:2])*60 + int(self.en[3:])
        return  kt-bd

    def Time(self):
        return '{} gio {} phut'.format(self.time//60, self.time%60)
    def __str__(self):
        return '{} {} {}'.format(self.id, self.name, self.Time())

arr = []
for i in range(int(input())):
    gmer = GMer(input(),input(),input(),input())
    arr.append(gmer)

arr.sort(key=lambda x: -x.time)
for i in arr:
    print(i)
    


