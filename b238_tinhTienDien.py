class Bill:
    def __init__(self, id, name, type, start, end):
        self.id = id
        self.name = name
        self.type = type
        self.start = start
        self.end = end
        
        self.setLimit()
        self.calculate()

    def setLimit(self):
        if type == 'A':
            self.limit = 100
        elif type == 'B':
            self.limit = 500
        elif type == 'C':
            self.limit = 200
            
    def calculate(self):
        sodien = self.end -self.start
        if sodien <= self.limit:
            self.inLimit = sodien*450
            self.overLimit = 0
            self.vat = 0
        else:
            self.inLimit = self.limit*450
            self.overLimit = (sodien-self.limit)*1000
            self.vat = self.overLimit//20
        self.total = self.inLimit+self.overLimit+self.vat
    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.id, self.name, self.inLimit, self.overLimit, self.vat, self.total)

arr = []
for i in range(int(input())):
    id = 'KH0{}'.format(i+1)
    name = ' '.join(input().split()).title()
    tmp = input().split()
    type = str(tmp[0])
    start = int(tmp[1])
    end = int(tmp[2])
    arr.append(Bill(id, name, type, start, end))
arr.sort(key=lambda x: -x.total)
for i in arr:
    print(i)
