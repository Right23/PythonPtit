class Biker:
    def __init__(self, name, unit, en):
        self.name = name
        self.unit = unit
        self.en = en
    def get_id(self):
        tmp1 = (self.name).split()
        tmp2 = (self.unit).split()
        res = ""
        for i in tmp2:
            res += i[0]
        for i in tmp1:
            res += i[0]
        return res
    def get_speed(self):
        tmp = (self.en).split(":")
        en = int(tmp[0])*3600+int(tmp[1])*60
        time = (en-6*3600)/3600
        return round(120/time)
    def __str__(self):
        return '{} {} {} {} Km/h'.format(self.get_id(), self.name, self.unit, self.get_speed())

arr = []
for i in range(int(input())):
    name = input().strip() 
    unit = input().strip() 
    en = input().strip() 
    arr.append(Biker(name, unit, en))
arr.sort(key=lambda x: x.en)
for i in arr:
    print(i)