from math import*

class  PS:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def __add__(self, other):
        mc = self.mau*other.mau//(gcd(self.mau, other.mau))
        self.tu *= (mc//self.mau)
        other.tu *= (mc//other.mau)
        self.tu += other.tu
        self.mau = mc
        return PS(self.tu, self.mau)
    def rut_gon(self):
        ucln = gcd(self.tu, self.mau)
        self.tu//=ucln
        self.mau//=ucln
    def __str__(self):
        return f'{self.tu}/{self.mau}'
if __name__ == '__main__':
    tu1, mau1, tu2, mau2 = map(int, input().split())
    p1 = PS(tu1, mau1)
    p2 = PS(tu2, mau2)
    p = p1+p2
    p.rut_gon()
    print(p)