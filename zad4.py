#!/usr/bin/python3

name = str(input('Podaj słowo: '))


frame1 = '---'
frame2 = '+'
frame3 = '|'

a = []
b = []

for char in name:
    a.append('{}{}'.format(frame2, frame1))
    b.append('{}{}'.format(frame3, char[0].center(3)))

a.append('{}'.format(frame2))
b.append('{}'.format(frame3))

print(''.join(a))
print(''.join(b))
print(''.join(a))
