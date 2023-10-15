class Rectangle:
    def __init__(self, l, w, c):
        self.l = l
        self.w = w
        self.c = c
    def getL(self):
        return self.l
    def getW(self):
        return self.w
    def color(self):
        return self.c.title()
    def perimeter(self):
        # return 2*(self.getL()+self.getW())
        return (self.l+self.w)>>1
    def area(self):
        return self.getL()*self.getW()
    
arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print('INVALID')