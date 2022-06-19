word = input()
password = ''
for ch in word:
    if ch == 'i':
        password = password + '!'
    elif ch == 'a':
        password = password + '@'
    elif ch == 'm':
        password = password + 'M'
    elif ch == 'B':
        password = password + '8'
    elif ch == 'o':
        password = password + '.'
    else:
        password = password + ch
print(password + 'q*s')
