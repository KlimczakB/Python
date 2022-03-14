#!/usr/bin/python

S = 'water air fire\n air water air fire earth air'

a = S.split()

print('The number of black characters in string')
print(sum(len(words) for words in a))

print('The number of words in string')
print(len(a))

print('The longest word in string')
print(max(a, key = len))

print('The lexicographic order')
print(sorted(a))

print('The length order')
print(sorted(a, key = len))
