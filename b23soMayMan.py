from math import*
def check(x):
    cnt = 0
    while(x>0):
        if(x%10 ==4 or x%10 ==7):
            cnt+=1
        x//=10
    if(cnt==4 or cnt==7):
        print("YES")
    else:
        print("NO")
    # print(cnt)
if __name__ == '__main__':
    n = int(input())
    check(n)