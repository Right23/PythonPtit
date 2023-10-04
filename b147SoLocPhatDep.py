def check(s):
    if s[0]=='8':
        return "NO"
    for i in s:
        if i!='6' and i != '8':
            return "NO"
    return "YES"
s = input()
print(check(s))