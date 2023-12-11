def getItem(d):
    return d.items()
if __name__=='__main__':
    s = input()
    k = int(input())
    
    d = dict()
    for i in range(0, len(s)-1, 2):
        tmp = s[i:i+2]
        if tmp in d:
            d[tmp]+=1
        else:
            d[tmp]=1
    a = list(d.keys())    
    a.sort()
    # so cac so thoa man
    cnt = 0
    for x in a:
        if d[x]>=k:
            cnt+=1
            print(x, d[x])
    if cnt == 0:
        print('NOT FOUND')
        