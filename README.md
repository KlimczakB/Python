# Python
EXERCISE 4.1

Let p=(x,y) be a point in a plane. Define the following functions using lambda:
(a) a test if p is in unit circle,
(b) a test if the coordinates of p are positive,
(c) a sorting key (y decreasing, x increasing),
(d) a sorting key (the sum |x|+|y|).

Using sorting keys: `point_list.sort(key=lambda p: ...)`

EXERCISE 4.2

Reversing a part of a list in place, reverse_range(L, left, right), the right index is included. Write iterative and recursive versions.
```
# Example
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reverse_range(L, 3, 6)   # index 6 is included!
print(L)   # [0, 1, 2, 6, 5, 4, 3, 7, 8, 9]   # the list L changed
# The numbers outside the range are intact.
```
EXERCISE 4.3

Create the following infinite generators:
(a) iter_even(), producing even numbers (0, 2, 4, ...),
(b) iter_odd(), producing odd numbers (1, 3, 5, ...),
(c) iter_power(k), producing powers of k (1, k, k*k, k*k*k, ...).
