#!/usr/bin/python3

t = (2, 4)
#print(t[2])
print('Nie można wykonać komendy print(t[2}) bo utworzona krotka zawiera \ntylko 2 obiekty t[0] i t[1]\n')
#t.append(6)
print('Do krotki nie można dodawać obiektów bo jest niezmienialna(immutable)\n')

print('Obiekty w krotce można przypisać do zmiennych')
a, b = t ; print(a, b)
