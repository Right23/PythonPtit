from decimal import Decimal
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        res = sqrt((self.x - other.x)** 2 + pow(self.y - other.y, 2))
        return res

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return f'{self.x} {self.y}'



if __name__ == '__main__':
    for t in range(int(input())):
        ax, ay, bx, by, cx, cy = map(float, input().split())
        pa = Point(ax, ay)
        pb = Point(bx, by)
        pc = Point(cx, cy)
        a = pa.distance(pb)
        b = pa.distance(pc)
        c = pb.distance(pc)
        if (a+b>c) and (a+c>b) and (b+c>a):
            s = a+b+c
            print('{:.3f}'.format(s))
        else:
            print("INVALID")