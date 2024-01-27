from datetime import *
class Customer:
    def __init__(self, id, name, room, num_day, bonus):
        self.id = id
        self.name = name
        self.room = room
        self.num_day = num_day
        self.bonus = bonus
    def get_price(self):
        price = 0
        if self.room[0]=='1':
            price = 25
        elif self.room[0]=='2':
            price = 34
        elif self.room[0]=='3':
            price = 50
        else:
            price = 80
        return (price * self.num_day) + self.bonus
    def __str__(self):
        return '{} {} {} {} {}'.format(self.id, self.name, self.room, self.num_day, self.get_price())
arr = []
for i in range(int(input())):
    id = 'KH{:02}'.format(i+1)
    name = input().strip()
    room = input().strip()
    i = datetime.strptime(input().strip(), '%d/%m/%Y')
    o = datetime.strptime(input().strip(), '%d/%m/%Y')
    num_day = (o-i).days + 1
    bonus = int(input().strip())
    arr.append(Customer(id, name, room, num_day, bonus))
arr.sort(key=lambda x: -x.get_price())
for i in arr:
    print(i)
