from sys import stdin
if __name__=='__main__':
    for line in stdin:
        tmp = ''
        for x in line.split():
            if x[-1]=='?' or x[-1]=='!' or x[-1]=='.':
                tmp += x[:-1]
                print(tmp.strip().capitalize())
                tmp = ''
            else:
                tmp += x+' '
        