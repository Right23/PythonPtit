from datetime import *
i = datetime.strptime(input().strip(), '%h:%m:%s')
o = datetime.strptime(input().strip(), '%h:%m:%s')
print(i.minutes, o.minutes)
# num_day = (o-i).days + 1