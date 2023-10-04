class Student:
    def __init__(self, name, dob, m1, m2, m3):
        self.name = name
        self.dob = dob
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def getTong(self):
        return '{:.1f}'.format(self.m1+self.m2+self.m3)
    def __str__(self):
        return f'{self.name} {self.dob} {self.getTong()}'
if __name__ == '__main__':
    name = str(input())
    dob = str(input())
    m1 = float(input())
    m2 = float(input())
    m3  = float(input())
    a = Student(name, dob, m1, m2, m3)
    print(a)

    