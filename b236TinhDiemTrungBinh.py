class sv:
    def __init__(self, id, name, m1, m2, m3):
        self.id = (id)
        self.name = name
        self.mark = (m1+m2+m3)/3
        self.rank 
    def __str__(self):
        return '{} {} {}'.format(self.id, self.name, self.mark)
arr = []
for i in range(int(input().strip())):
    id = 'TS{:02}'.format(i+1)
    tmp = input().strip().split()
    name = ""
    for i in tmp:
        name += i.title()+" "
    m1 = float(input())
    m2 = float(input())
    m3 = float(input())
    arr.append(sv(id, name, m1, m2, m3))
    
arr.sort(key=lambda x: (-x.mark, x.id))
list_rank = [int(i) for i in range(1, 21)]


for i in arr:
    print(i, rank[i], sep=' ')