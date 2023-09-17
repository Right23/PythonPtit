n = int(input())
a = [int(i) for i in input().split()]
res = 0
a.sort()
m1 = max(a[0]*a[1], a[len(a)-2]*a[len(a)-1])
m2 = max(a[0]*a[1]*a[len(a)-1], a[len(a)-1]*a[len(a)-2]*a[len(a)-3])
print(max(m1, m2))