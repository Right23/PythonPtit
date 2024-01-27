arr = []
for t in range(int(input())):
    s = input()
    nums = ''
    for x in s:
        if x.isdigit():
            nums += x
        else:
            nums += ' '
    arr.extend([int(x) for x in nums.split()])
                
for i in sorted(arr):
    print(i)