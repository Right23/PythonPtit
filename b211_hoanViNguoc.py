x = []*101
global n
used = []*101
def inkq():
    for i in range(1, n+1):
        print(x[i], end='')
    print()
def Try(i):
    for j in range(1, n+1):
        if not used[j]:
            x[i] = j
            used[j] = True
            if i == n:
                inkq()
            else:
                Try(i+1)
            used[j] = False
if __name__=='__main__':
    n = int(input())
    used = [False for i in range(1, 101)]
    Try(1)

    
