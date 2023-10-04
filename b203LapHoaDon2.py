from datetime import datetime
class Customer:
    def __init__(self, id, name, id_room, bonus, num_day):
        self.id = id
        self.name = name
        self.id_room = id_room
        self.bonus = bonus
        self.num_day = num_day
    def get_price(self):
        total = 0
        price = 0
        if self.id_room[0]=="1":
            price = 25
        elif self.id_room[0]=="2":
            price = 34
        elif self.id_room[0]=="3":
            price = 50
        elif self.id_room[0]=="4":
            price = 80
        total = price*self.num_day+self.bonus
        return total
    def __str__(self):
        return '{} {} {} {} {}'.format(self.id, self.name, self.id_room, self.num_day, self.get_price())

arr = []
for i in range(int(input())):
    id = 'KH{:02}'.format(i+1)
    name = input().strip()
    id_room = input().strip()
    i = datetime.strptime(input().strip(), '%d/%m/%Y')
    o = datetime.strptime(input().strip(), '%d/%m/%Y')
    num_day = (o-i).days + 1
    bonus = int(input().strip())
    cus = Customer(id, name, id_room, bonus, num_day)
    arr.append(cus)
arr.sort(key=lambda x: -x.get_price())
for i in arr:
    print(i)
