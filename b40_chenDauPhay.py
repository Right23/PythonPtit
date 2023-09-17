def solve():
    s = str(input())
    for i in range(len(s)-3, 0, -3):
        s = s[:i] + ',' + s[i:]
    print(s)

if __name__ == '__main__':
    solve()
