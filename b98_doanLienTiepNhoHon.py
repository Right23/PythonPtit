for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    st, res = [], [0]*n
    for i in range(n):
        while(len(st)>0 and a[i]>=a[st[-1]]):
            st.pop()
        res[i] = i+1 if len(st)==0 else i-st[-1]
        st.append(i)
    print(*res)
