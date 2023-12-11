n, m = map(int, input().split())
a = [x for x in input().split()]

# so phieu bau
se = set([a.count(x) for x in a])
se.remove(max(se))

if len(se)==0:
    print('NONE')
else:
    ma = max(se)
    for x in a:
        if a.count(x)==ma:
            print(x)
            break
    