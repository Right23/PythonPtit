class sv:
    def __init__(self, id, name, mark, dantoc, kv):
        self.id = (id)
        self.name = name
        self.mark = mark
        self.dantoc = dantoc
        self.kv = kv
    def bonus(self):
        add = 0
        if self.kv == "1":
            add+= 1.5
        elif self.kv == "2":
            add+= 1
        if self.dantoc != "Kinh":
            add+= 1.5
        return add
    def status(self):
        bench_mark = 20.5
        if self.mark + self.bonus() >= bench_mark:
            return "Do"
        return "Truot"
    def __str__(self):
        return '{} {} {:.1f} {}'.format(self.id, self.name, self.mark+self.bonus(), self.status())
arr = []
for i in range(int(input().strip())):
    id = 'TS{:02}'.format(i+1)
    tmp = input().strip().split()
    name = ""
    for i in tmp:
        name += i.title()+" "
   
    mark = float(input().strip())
    dantoc = input().strip()
    kv = input().strip()
    arr.append(sv(id, name, mark, dantoc, kv))
arr.sort(key=lambda x: (-(x.mark+x.bonus()), x.id))
for i in arr:
    print(i)