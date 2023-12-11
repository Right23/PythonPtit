def Phi(type, num_seat):
    if type=='Xe_con':
        if num_seat=='5':
            return 10000
        return 15000
    elif type=='Xe_tai':
        return 20000
    elif type == 'Xe_khach':
        if num_seat == '29':
            return 50000
        return 70000
if __name__ == '__main__':
    n = int(input())
    d = dict()
    for _ in range(n):
        a = input().split()
        if a[3]=='IN':
            if a[4] in d:
                d[a[4]]+=Phi(a[1], a[2])
            else:
                d[a[4]]=Phi(a[1], a[2])
    for key, value in d.items():
        # print(key, value, sep=': ')
        print(f'{key}: {d[key]}')
        