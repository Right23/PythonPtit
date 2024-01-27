from math import *
class sv:
    def __init__(self, id, name, m1, m2, m3):
        self.id = (id)
        self.name = name
        self.mark = round(((m1*3+m2*3+m3*2)/8 + 0.001), 3)
    def get_mark(self):
        return self.mark
    def get_id(self):
        return self.id
    def __str__(self):
        return '{} {} {:.2f}'.format(self.id, self.name, self.mark)
arr = []
for i in range(int(input().strip())):
    id = 'SV{:02}'.format(i+1)
    tmp = input().strip().split()
    name = ""
    for i in tmp:
        name += i.title()+" "
    m1 = float(input())
    m2 = float(input())
    m3 = float(input())
    arr.append(sv(id, name, m1, m2, m3))
    
arr.sort(key=lambda x: (-x.mark, x.id))
list_rank = dict()
for i in range(len(arr)):
    list_rank[arr[i].id] = i+1
# for i in list_rank.items():
#     print(i)

for i in range(1, len(arr)):
    if arr[i].get_mark() == arr[i-1].get_mark():
        list_rank[arr[i].get_id()] = list_rank[arr[i-1].get_id()]

for i in arr:
    print(i, list_rank[i.get_id()], sep=' ')