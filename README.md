# Python
## EXERCISE 2.1

Create a long positive integer. Find the number of zeros. Hint: change the number to a string.

## EXERCISE 2.2 (BOOL)
```
# Explain the results.
x = 5
x == 5 and 3                  # 3
x == 4 and 3                  # False
3 and x == 5                  # True
3 and x == 4                  # False

isinstance(True, int)         # True
isinstance(True, bool)        # True
```
## EXERCISE 2.3 (NUMBERS)

Find the sum `1*1 + 3*3 + 5*5 + ... + 2021*2021 [hint: use sum()]`.

## EXERCISE 2.4 (STR)

(a) Find Unicode code points (int) for all characters of your name.
`Example: "Andrzej" --> [65, 110, 100, 114, 122, 101, 106]`

(b) Prepare the periodic table (ten elements) as a list
`pt = [(1,"Hydrogen","H",1), (2,"Helium","He",4), ...].`
Use pt to print a table (3 right + 20 left + 6 center + 10 right)
```
+---+--------------------+------+----------+
|No.|Name (en)           |Symbol|Weight (u)|
+---+--------------------+------+----------+
|  1|Hydrogen            |  H   |         1|
|  2|Helium              |  He  |         4|
|   | ...                |      |          |
+---+--------------------+------+----------+
```
## EXERCISE 2.5 (LIST)

Let S be a long string (many lines).

Find the number of black characters in S [not whitespace, see the method `S.isspace()`].

Find the number of words in S (a word is a sequence of black characters).

Find the longest word in S.

Sort words from S according to (1) the lexicographic order, (2) the length.

## EXERCISE 2.6 (TUPLE)
```
# Find and explain the results.
t = (2, 4)
print(t[2])
t.append(6)
a, b = t ; print(a, b)
```
## EXERCISE 2.7 (DICT)

Create a dict for conversion of roman numerals (I, IV, V, IX, X, XL, L, XC, C, CD, D, CM, M) to arabic numbers. Use different methods.
