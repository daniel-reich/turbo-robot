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
  h1, m1, s1, h2, m2, s2 = lst
  pal_minutes = [0, 11, 22, 33, 44, 55]
  inv = lambda n: (n % 10) * 10 + (n // 10)
  totime = lambda h, m, s: h * 3600 + m * 60 + s
  t1,t2 = totime(h1, m1, s1), totime(h2, m2, s2) 
  count = 0
  for H in range(h1, h2 + 1):
    S = inv(H)
    if S < 60:
      for M in pal_minutes:
        T = totime(H, M, S)
        if t1 <= T and T <= t2:
          count += 1
  return count

