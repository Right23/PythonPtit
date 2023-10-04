from decimal import Decimal
from math import*

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # def __init__(self, p):
    #     self.x = p.x
    #     self.y = p.y
    def distance(self, other):
        res = sqrt(pow(self.x-other.x, 2)+pow(self.y-other.y, 2))
        return '{:.4f}'.format(res)
    def __str__(self):
        return f'{self.x} {self.y}'
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t-=1
         