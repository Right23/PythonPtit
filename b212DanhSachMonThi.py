class subject:
    def __init__(self, id, name, mth):
        self.id = id
        self.name = name
        self.mth = mth
    def __str__(self):
        return '{} {} {}'.format(self.id, self.name, self.mth)
arr = []
for t in range(int(input())):
    id = input()
    name = input()
    mth = input()
    arr.append(subject(id, name, mth))
arr.sort(key= lambda x: x.id)
for i in arr:
    print(i)