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

from datetime import datetime, timedelta
def palindrome_time(lst):
  t1=datetime(2020,11,1,lst[0], lst[1], lst[2])
  t2=datetime(2020,11,1,lst[3], lst[4], lst[5])
  td=timedelta(seconds=1)
  if t1==t2:
    if datetime.strftime(t1,'%H:%M:%S')==datetime.strftime(t1,'%H:%M:%S')[::-1]:
      return 1
    else:
      return 0
  else:
    c=0
    while t1!=t2:
      if datetime.strftime(t1,'%H:%M:%S')==datetime.strftime(t1,'%H:%M:%S')[::-1]:
        c+=1
      t1+=td  
    if datetime.strftime(t2,'%H:%M:%S')==datetime.strftime(t2,'%H:%M:%S')[::-1]:
      c+=1
    return c

