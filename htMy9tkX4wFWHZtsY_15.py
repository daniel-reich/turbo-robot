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
  import datetime as dt
  start = dt.datetime(1,1,1, lst[0], lst[1], lst[2])
  end = dt.datetime(1,1,1, lst[3], lst[4], lst[5])
  count = 0
  t = start
  while t <= end:
    if str(t.time()) == str(t.time())[::-1]:
      count += 1
    t += dt.timedelta(seconds=1)
  return count

