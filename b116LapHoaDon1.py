class Customer:
    def __init__(self, id, name, kwh):
        self.id = id
        self.name = name
        self.kwh = kwh
    def get_Total(self):
        tmp = self.kwh
        total = 0
        if tmp > 100:
            total += (tmp-100)*200
            tmp = 100
        if tmp > 50:
            total += (tmp-50)*150
            tmp = 50
        if tmp > 0:
            total += tmp *100
            tmp = 0
        if self.kwh > 100:
            total *= 1.05
        elif self.kwh > 50:
            total *= 1.03
        else:
            total *= 1.02
        return total
    def __str__(self):
        return '{} {} {}'.format(self.id, self.name, '{:.0f}'.format(self.get_Total()))

arr = []        
for i in range(int(input())):
    id = 'KH{:02}'.format(i+1)
    name = input()
    cu = int(input())
    moi = int(input())
    kwh = moi-cu
    c = Customer(id, name, kwh)
    arr.append(c)
arr.sort(key=lambda x: -x.get_Total())
for i in arr:
    print(i)

