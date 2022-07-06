#!/usr/bin/python3

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def reverse_range(L, left, right):
    if left < right:
        x = L[left]
        L[left] = L[right]
        L[right] = x
        left += 1
        right -= 1

reverse_range(L, 3, 6)
print(L)
