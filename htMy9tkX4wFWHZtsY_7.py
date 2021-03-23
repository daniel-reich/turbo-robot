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

import datetime
def palindrome_time(lst):
  ts = datetime.datetime(100, 1, 1, lst[0], lst[1], lst[2])
  end = datetime.datetime(100, 1, 1, lst[3], lst[4], lst[5])
  cnt = 0
  
  while ts <= end:
    tstr = ts.strftime("%H:%M:%S")
    cnt += tstr == tstr[::-1]
    ts += datetime.timedelta(0, 1)
  return cnt

