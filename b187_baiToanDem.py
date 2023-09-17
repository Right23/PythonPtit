n = int(input())
a = []
while True:
    s = input()
    k = [int(i) for i in s.split()]
    a.extend(k)
    if len(a)==n:
        break
    
c = []
cnt = 0
for i in range(1, max(a)+1):
    if i not in a:
        c.append(i)
        cnt+=1
if cnt==0:
    print("Excellent!")
else:
    for i in c:
        print(i)