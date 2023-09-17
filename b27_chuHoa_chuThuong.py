def convert():
    s = str(input())
    h = t = 0
    for i in range(0, len(s)):
        if s[i].islower():
            t+=1
        else:
            h+=1
    if(t>=h):
        print(s.lower())
    else:
        print(s.upper())
if __name__ == '__main__':
    convert()