from math import*

class  PS:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def rut_gon(self):
        ucln = gcd(self.tu, self.mau)
        self.tu//=ucln
        self.mau//=ucln
    def __str__(self):
        return f'{self.tu}/{self.mau}'
if __name__ == '__main__':
    tu, mau = map(int, input().split())
    p = PS(tu, mau)
    p.rut_gon()
    print(p)