import functools
class DanhBa:
    def __init__(self, name, sdt, ngayGoi):
        self.name = name
        self.sdt = sdt
        self.ngayGoi = ngayGoi
    def __str__(self):
        return self.name+': '+self.sdt+' '+self.ngayGoi
def cmp(a, b):
    arr1, arr2 = a.name.split(), b.name.split()
    i, j = len(arr1)-1, len(arr2)-1
    while(i>=0 and j >=0):
        if arr1[i] != arr2[j]:
            return arr1[i]< arr2[j]
        i-=1
        j -=1
        
if __name__=='__main__':
    f = open('SOTAY.txt')
    ngayGoi = ''
    a = []
    while True:
        line = f.readline().strip()
        if not line: break
        if line.startswith('Ngay'):
            ngayGoi = line[5:]
        else:
            name = line
            sdt = f.readline().strip()
            a.append(DanhBa(name, sdt, ngayGoi))
    for x in sorted(a, key=functools.cmp_to_key(cmp)):
        print(x)

        