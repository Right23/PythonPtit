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
            res+=i[0]
        for i in tmp1:
            res+=i[0]
        return res
    def get_result(self):
        st = 6*60*60
        tmp = (self.en).split(":")
        en = int(tmp[0])*3600+int(tmp[1])*60
        # en = int(self.en[0:1])*3600+int(self.en[2:])*60
        time =  (en-st)/3600
        return round(120/time)
    def __str__(self):
        return '{} {} {} {} Km/h'.format(self.get_id(), self.name, self.unit, (self.get_result()))
arr = []
for i in range(int(input())):
    name = input().strip()
    unit = input().strip()
    en = input().strip()
    biker = Biker(name, unit, en)
    arr.append(biker)
arr.sort(key= lambda x: x.en)
for i in arr:
    print(i)
    
    
        


