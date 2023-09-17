import string
d = dict({})
b=[]
for t in range(int(input())):
    text = input()
    text = text.translate(str.maketrans("","", string.punctuation))
    a = text.lower().split()
    e = dict({})
    for x in a:
        if x in e:
            e[x]+=1
        else:
            e[x] = 1
    for x in d:
        if x in e:
            d[x] +=e[x]
    # d.update(e)
    c = list(d.items())
    c.sort(key= lambda x:(-x[1], x[0]))
    b.extend(c)
for x in b:
    print(x)
    # for k, v in d.items():
    #     print(k, v, sep=' ')
