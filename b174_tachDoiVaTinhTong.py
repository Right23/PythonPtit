def ghepDs(a):
    sum = 0
    for i in range(len(a)):
        sum = sum*10+i
    return sum
n = int(input())
while n > 0:
    tmp = str(n)
    a = tmp[0:len(tmp)//2]
    b = tmp[len(tmp)//2:]
    print(ghepDs(a), ghepDs(b), sep=' ')
    n = ghepDs(a)+ghepDs(b)
    print(n)
