"""


Create a function that counts number of palindromes within two timestamps
inclusive. A palindrome is a timestamp that can be read the same from left to
right and from right to left (e.g. `02:11:20`).

### Examples

    palindrome_time([2, 12, 22, 4, 35, 10]) ➞ 14
    
    palindrome_time([12, 12, 12, 13, 13, 13]) ➞ 6
    
    palindrome_time([6, 33, 15, 9, 55, 10]) ➞ 0

### Notes

Input list contains six numbers `[h1, m1, s1, h2, m2, s2]` for begin and end
timestamps.

"""

def palindrome_time(lst):
  im = sum([1 for i in range(lst[0], lst[3]) if i < 6 or (i > 9 and i < 16) or i > 19 ])
  im -= 1
  mt1 = 0
  mt2 = 0
  if im >= 0:
    for it in range(0, 56, 11):
      if it >= lst[1]: mt1 += 1
      if it <= lst[4]: mt2 += 1
  elif im == -1:
    im = 0
    for it in range(lst[1], lst[3], 1):
        if it >= lst[1] and it % 11 == 0: mt1 += 1
  return im*6 + mt1 + mt2

