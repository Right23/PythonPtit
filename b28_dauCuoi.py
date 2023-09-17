def check():
    t = int(input())
    while(t>0):
        s = str(input())
        begin = s[0:2:1]
        end = s[len(s)-2:len(s):1]
        # print(begin, end)
        if(begin==end):
            print("YES")
        else:
            print("NO")
        t-=1
if __name__ == '__main__':
    check() 