# 1792816 Anthony Flores 11.18

f = input()
lth = [int(x)for x in f.split(' ') if int(x)>=0]
lth.sort()
for x in lth:
    print(x, end=' ')
