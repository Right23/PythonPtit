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
        return self.caThi.get_ngayThi()+' '+self.caThi.get_gioThi()+' '+self.caThi.get_phongThi()+' '+self.monThi.get_tenMon()+' '+self.maNhom+' '+self.soSv
if __name__=='__main__':
    f = open("MONTHI.in", "r")
    d_monThi =dict()
    n = int(f.readline())
    for i in range(0, n):
        maMon = (f.readline())
        tenMon = f.readline()
        hinhThuc = f.readline()
        d_monThi[maMon] = MonThi(maMon, tenMon, hinhThuc)
        f.close()
        
    c = open("CATHI.in", "r")
    d_caThi = dict()
    n = int(c.readline())
    for i in range(0, n):
        maCa = 'C{:03}'.format(i+1)
        ngayThi = c.readline()
        gioThi = c.readline()
        phongThi = c.readline()
        d_caThi[maCa] = CaThi(i+1,ngayThi, gioThi, phongThi)
        c.close()
        
    l = open("LICHTHI.in", "r")
    arr = []
    n = int(l.readline())
    while n > 0:
        maCa = l.readline()
        maMon = l.readline()
        maNhom = l.readline()
        soSv = int(l.readline())
        arr.append(LichThi(d_caThi(maCa), d_monThi(maMon), maNhom, soSv))
        n -= 1
    for x in arr:
        print(x)