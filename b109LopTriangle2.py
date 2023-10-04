from decimal import Decimal
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        res = sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))
        return res

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return f'{self.x} {self.y}'


class Triangle:
    def __init__ (self, a=Point(0, 0), b=Point(0, 0), c=Point(0, 0)):
        self.a = a
        self.b = b
        self.c = c

    def valid(self):
        ab = sqrt(pow(self.b.getX() - self.a.getX(), 2) + pow(self.b.getY() - self.a.getY(), 2))
        bc = sqrt(pow(self.b.getX() - self.c.getX(), 2) + pow(self.b.getY() - self.c.getY(), 2))
        ca = sqrt(pow(self.c.getX() - self.a.getX(), 2) + pow(self.c.getY() - self.a.getY(), 2))
        if (ab + bc > ca) and (bc + ca > ab) and (ca + ab > bc):
            return True
        return False

    def getPerimeter(self):
        ab = sqrt(pow(self.b.getX() - self.a.getX(), 2) + pow(self.b.getY() - self.a.getY(), 2))
        bc = sqrt(pow(self.b.getX() - self.c.getX(), 2) + pow(self.b.getY() - self.c.getY(), 2))
        ca = sqrt(pow(self.c.getX() - self.a.getX(), 2) + pow(self.c.getY() - self.a.getY(), 2))
        return '{:.3f}'.format(ab + ca + bc)


if __name__ == '__main__':
    for t in range(int(input())):
        ax, ay, bx, by, cx, cy = map(float, input().split())
        pa = Point(ax, ay)
        pb = Point(bx, by)
        pc = Point(cx, cy)
        a = pa.distance(pb)
        b = pa.distance(pc)
        c = pb.distance(pc)
        if (a+b>c) and(a+c>b) and(b+c>a):
            s = (1/4)*sqrt((a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c))
            print('{:.2f}'.format(s))
        else:
            print("INVALID")