class MH:
    def __init__(self, id, name, amount, price, discount):
        self.id = id
        self.name=name
        self.amount=amount
        self.price = price
        self.discount = discount
    def get_cost(self):
        return self.price*self.amount - self.discount
    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.id, self.name, self.amount, self.price, self.discount, self.get_cost())
arr = []
for t in range(int(input().strip())):
    id = input().strip()
    name = input().strip()
    amount = int(input().strip())
    price = int(input().strip())
    discount = int(input().strip())
    mh = MH(id, name, amount, price, discount)
    arr.append(mh)
arr.sort(key=lambda x: -x.get_cost())
for i in arr:
    print(i)

    
