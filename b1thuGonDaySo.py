n = int(input())
a = list(int(i) for i in input().split())
# a = [i for i in input().split()]
i = 1
while(i<len(a)):
    if (a[i]+a[i-1])%2==0:
        a.pop(i)
        a.pop(i-1)
        if i>1:
            i-=1
    else:
        i+=1
print(len(a))
# Elpulga