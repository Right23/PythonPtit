class nv:
    def __init__(self, id, name, base, wd):
        self.id = id
        self.name = name
        self.base = base
        self.wd = wd
        self.dept_name = ''
    def set_dept_name(self, str):
        self.dept_name = str
    def get_salary(self):
        k = 0
        type = self.id[:1]
        yrs = int(self.id[1:3:1])
        if type =='A':
            if yrs > 16:
                k = 20
            elif yrs >= 9:
                k = 14
            elif yrs >= 4:
                k = 12
            elif yrs >= 1:
                k = 10
        elif type =='B':
            if yrs > 16:
                k = 16
            elif yrs >= 9:
                k = 13
            elif yrs >= 4:
                k = 11
            elif yrs >= 1:
                k = 10
        elif type =='C':
            if yrs > 16:
                k = 14
            elif yrs >= 9:
                k = 12
            elif yrs >= 4:
                k = 10
            elif yrs >= 1:
                k = 9
        elif type =='D':
            if yrs > 16:
                k = 13
            elif yrs >= 9:
                k = 11
            elif yrs >= 4:
                k = 9
            elif yrs >= 1:
                k = 8
        return k*self.wd*self.base*1000
    def __str__(self):
        return '{} {} {} {}'.format(self.id, self.name, self.dept_name, self.get_salary())
d = dict()
for i in range(int(input())):
    line = [x for x in input().split()]
    tmp = ''
    for j in range(1, len(line)):
        tmp += line[j]
        if j < len(line)-1:
            tmp += ' '
    d[line[0]] = tmp
arr = []
for i in range(int(input())):
    id = input().strip()
    name = input().strip()
    base = int(input().strip())
    wd = int(input().strip())
    x = nv(id, name, base, wd)
    x.set_dept_name(d[id[-2:]])
    arr.append(x)
# arr.sort(key=lambda x: -x.get_salary())
for i in arr:
    print(i)
