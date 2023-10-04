class SoPhuc:
    def __init__(self, re, im):
        self.re = re
        self.im = im
    def __add__(self, other):
        tmp1 = self.re+other.re
        tmp2 = self.im + other.im
        return SoPhuc(tmp1, tmp2)
    def __mul__(self, other):
        tmp1 = self.re*other.re-self.im*other.im
        tmp2 = self.re*other.im+self.im*other.re
        return SoPhuc(tmp1, tmp2)
    def __str__(self):
        if self.im >= 0:
            return f'{self.re} + {self.im}i'
        return f'{self.re} - {-self.im}i'
if __name__ == '__main__':
    for t in range(int(input())):
        r1, i1, r2, i2 = map(int, input().split())
        a = SoPhuc(r1, i1)
        b = SoPhuc(r2, i2)
        c = (a+b)*a
        d = (a+b)*(a+b)
        print(c, d, sep=', ')
