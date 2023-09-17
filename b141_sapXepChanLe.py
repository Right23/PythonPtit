n = int(input())
a = [int(i) for i in input().split()]
c = []
id_c = []
l = []
id_l = []
for i in range(n):
    if a[i]%2!=0:
        l.append(a[i])
        id_l.append(i)
    else:
        c.append(a[i])
        id_c.append(i)

l.sort(reverse=True)
c.sort()
res = []*n
le = 0
chan = 0
for i in id_l:
    if le == len(l):
        break
    res[i] = l[le]
    le+=1
for i in id_c:
    if chan==len(c):
        break
    res[i] = c[chan]
    chan+=1

print(*res)

# mi = min(len(c), len(l))
# for i in range(mi):
#     print(l[i], c[i], sep=' ', end=' ')
# if mi==len(c):
#     for i in range(mi, len(l)):
#         print(l[i], end=' ')
# else:
#     for i in range(mi, len(c)):
#         print(c[i], end=' ')
        