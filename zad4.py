#!/usr/bin/python3

#2.4a
name = 'Barbara'

for char in name:
    print('{} {}'.format(char, ord(char)))

#2.4b

frame1 = '+---+--------------------+------+----------+'
record = '|No.|Name (en)           |Symbol|Weight (u)|' 

elements = [(1,'Hydrogen','H',1), (2,'Helium','He',4), (3,'Lithium','Li',7), 
            (4,'Beryllium','Be',9), (5,'Boron','B',11), (6,'Carbon','C',12), 
            (7,'Nitrogen','N',14), (8,'Oxygen','O',16), (9,'Fluorine','F',19), 
            (10,'Neon','Ne',20)]

a = [frame1, record, frame1]

for i in elements:
    a.append('|{}|{}|{}|{}|'.format(str(i[0]).rjust(3), i[1].ljust(20), i[2].center(6), str(i[3]).rjust(10)))

a.append(frame1)

print('\n'.join(a))
