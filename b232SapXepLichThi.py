class MonThi:
    def __init__(self, maMon, tenMon, hinhThuc):
        self.maMon = maMon
        self.tenMon = tenMon
        self.hinhThuc = hinhThuc
    def get_maMon(self):
        return self.maMon
    def get_tenMon(self):
        return self.tenMon
    def get_hinhThuc(self):
        return self.hinhThuc
# 
class CaThi:
    def __init__(self, i, ngayThi, gioThi, phongThi):
        self.maCa = 'C{:03}'.format(i)
        self.ngayThi = ngayThi
        self.gioThi = gioThi
        self.phongThi = phongThi
    def get_maCa(self):
        return self.maCa
    def get_ngayThi(self):
        return self.ngayThi
    def get_gioThi(self):
        return self.gioThi
    def get_phongThi(self):
        return self.phongThi
    
    def get_date(self):
        date = ''
        tmp = self.ngayThi.split('/')
        for i in range(2, -1, -1):
            date += tmp[i]+'/'
        return date
# 
class LichThi:
    def __init__(self, caThi, monThi, maNhom, soSv):
        self.caThi = caThi
        self.monThi = monThi
        self.maNhom = maNhom
        self.soSv = soSv
    def get_MonThi(self):
        return self.monThi
    def get_CaThi(self):
        return self.caThi
    def get_MaNhom(self):
        return self.maNhom
    def get_SoSv(self):
        return self.soSv

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.caThi.get_ngayThi(), self.caThi.get_gioThi(), self.caThi.get_phongThi(), self.monThi.get_tenMon(), self.maNhom, self.soSv)

if __name__=='__main__':
    f = open("MONTHI.in", "r")
    d_monThi =dict()
    n = int(f.readline().strip())
    for i in range(n):
        maMon = f.readline().strip()
        tenMon = f.readline().strip()
        hinhThuc = f.readline().strip()
        d_monThi[maMon] = MonThi(maMon, tenMon, hinhThuc)
    f.close()
    # for key, value in d_monThi.items():
    #     print(key, value)
    
    c = open("CATHI.in", "r")
    d_caThi = dict()
    n = int(c.readline().strip())
    for i in range(0, n):
        maCa = 'C{:03}'.format(i+1)
        ngayThi = c.readline().strip()
        gioThi = c.readline().strip()
        phongThi = c.readline().strip()
        d_caThi[maCa] = CaThi(i+1,ngayThi, gioThi, phongThi)
    c.close()
    # for key, value in d_caThi.items():
    #     print(key, value)
        
    l = open("LICHTHI.in", "r")
    arr = []
    n = int(l.readline().strip())
    for i in range(n):
        a = l.readline().strip().split()
        maCa = a[0]
        maMon = a[1]
        maNhom = a[2]
        soSv = int(a[3])
        arr.append(LichThi(d_caThi[maCa], d_monThi[maMon], maNhom, soSv))
    l.close()
    arr.sort(key=lambda x: (x.get_CaThi().get_date(), x.get_CaThi().get_gioThi(), x.get_CaThi().get_maCa()))
    for x in arr:
        print(x)