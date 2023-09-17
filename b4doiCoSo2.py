def bin_to_qua(bin_num):
    qua_num = ""
    while bin_num > 0:
        remainder = bin_num%4
        qua_num = str(remainder)+qua_num
        bin_num//=4
    return qua_num
for t in range(int(input())):
    b = int(input())
    if b==2:
        print(bin(int(input(), 2))[2::])
    elif b==4:
        print(bin_to_qua(int(input(), 2)))
    elif b== 8:
        print(oct(int(input(), 2))[2::])
    elif b== 16:
        s = str(hex(int(input(), 2))[2::])
        for i in s:
            if i.isalpha():
                print(i.upper(), end='')
            else:
                print(i, end='')
        print()