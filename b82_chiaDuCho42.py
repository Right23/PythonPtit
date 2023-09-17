dd = [0]*42
cnt, res = 10, 0
while cnt!=0:
    a = [int(i) for i in input().split()]
    cnt-=len(a)
    for i in a:
        if dd[i%42]==0:
            res+=1
            dd[i%42]=1
print(res)
# dung set


# s = {43}
# n = 10
# while n!=0:
#     a = [int(i) for i in input().split()]
#     n-=len(a)
#     for i in a:
#         s.add(i%42)
# print(len(s)-1)