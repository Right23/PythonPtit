from functools import cmp_to_key
import re
word_count = {}
for t in range(int(input())):
    tmp = input().lower()
    # s = re.split(r",|-|!|\.|\?|/|:|' '|;", tmp)
    s = tmp.split()
    for x in s:
        if x in word_count:
            word_count[x] = +1
        else:
            word_count[x] = 1
sorted_word_count = sorted(word_count.items(), key=lambda x: -x[1])
for word, count in sorted_word_count:
    print(word, count, sep=' ')

    
