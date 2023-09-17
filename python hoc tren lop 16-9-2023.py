# 6.1
print('6.1')
d = {
    'first_name':'Minh',
    'last_name':'Nguyen',
    'age':'20',
    'city':'Ha Noi'
}
print(d)
# for key, value in d.items():
#     print(key, value, sep=' : ')
print('\n6.2')
# 6.2
p = {
    'a':'1',
    'b':'2',
    'c':'3',
    'd':'4',
    'e':'5'
}
for key, value in p.items():
    print(key, value, sep="'s favorite number is: ")
print('\n6.3')
# 6.3
a = {
    'int':'Integer',
    'str':'String',
    'chr':'character',
    'for':'loop',
    'if':'condition'
}
for key, value in a.items():
    print(key, value, sep=':', end='\n')
print('\n6.4')
# 6.4
for key, value in d.items():
    print(key, value, sep=' : ')
print('\n6.5')
# 6.5
river={
    'nile':'egypt',
    'red':'Viet Nam',
    'amazon':'brazil'
}
for key, value in river.items():
    print('The ' + key, value, sep=' runs through ')
for key in river.keys():
    print(key)
for value in river.values():
    print(value)
print('\n6.6')
# 6.6
ds={
    'an':'c',
    'binh':'c++',
    'minh':'java'
}
a = ['minh','son', 'ha', 'giang', 'an', 'binh']
for x in a:
    if x in ds.keys():
        print('Thanks for joining')
    else:
        print('Pleae join!')
print('\n6.7')
# 6.7
d1 = {
    'first_name':'Bich',
    'last_name':'Pham',
    'age':'10',
    'city':'TPHCM'
}
d2 = {
    'first_name':'Ha',
    'last_name':'Le',
    'age':'30',
    'city':'hai duong'
}
d3 = {
    'first_name':'Trong',
    'last_name':'Vu',
    'age':'50',
    'city':'Hai Phong'
}
peoples = []
peoples.append(d1)
peoples.append(d2)
peoples.append(d3)
for x in peoples:
    print(x)
for people in peoples:
    for key, value in people.items():
        print(key, value, sep=':')
    print()
# 6.8
print('\n6.8')
p1={
    'kind':'cat',
    'name':'Kitty',
    'owner':'Jonh'
}
p2 = {
    'kind':'dog',
    'name':'Nick',
    'owner':'Ronal'
}
pets = []
pets.append(p1)
pets.append(p2)
for pet in pets:
    for key, value in pet.items():
        print(key, value, sep=":")
    print()

# 6.10
print('\n6.10')
fav={
    'nam':[1, 2],
    'hung':[3, 4]
}
for key, value in fav.items():
    print(key, value, sep=':')