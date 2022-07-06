#!/usr/bin/python3

#2.1

for x in range(1,41):
    if x == 13:
        continue
    print('\nx =', x)
    if (x % 5 == 0 and x % 7 == 0):
        print('x is divided by 5 and 7')
    elif (x % 5 == 0):
        print('x is divided by 5')
    elif (x % 7 == 0):
        print('x is divided by 7')
    else:
        print('x is not important')

#2.2
y = 0

while y < 40:
    y += 1
    if y == 13:
        continue
    print('\n',y)
    if (y % 5 == 0 and y % 7 == 0):
        print('y is divided by 5 and 7')
    elif (y % 5 == 0):
        print('y is divided by 5')
    elif (y % 7 == 0):
        print('y is divided by 7')
    else:
        print('y is not important')

