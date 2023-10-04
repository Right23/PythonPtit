class Rectangle:
    def __init__(self, l, w, c):
        self.l = l
        self.w = w
        self.c = c
    def getL(self):
        return self.l
    def getW(self):
        return self.w
    def getC(self):
        return self.c.title()
    def perimeter(self):
        return 2*(self.getL()+self.getW())
    def area(self):
        return self.getL()*self.getW()
    
if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.getC()))
    