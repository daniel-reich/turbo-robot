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
  h1 = lst[0]
  m1 = lst[1]
  s1 = lst[2]
  h2 = lst[3]
  m2 = lst[4]
  s2 = lst[5]
  count = 0
  keepGoing = True
  while (keepGoing): 
    if ((h1 % 10) == (s1 // 10) and (s1 % 10) == (h1 // 10) and (m1 % 11) == 0):
      count = count + 1
    if h1 == h2 and m1 == m2 and s1 == s2:
      keepGoing = False
    s1 = s1 + 1
    if (s1 == 60):
      s1 = 0
      m1 = m1 + 1
      if (m1 == 60):
        m1 = 0
        h1 = h1 + 1
  return count

