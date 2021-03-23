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

from itertools import dropwhile,takewhile
def palindrome_time(lst):
  def string(h,m,s):
    s1 = str(m).rjust(2, '0')
    s2 = str(s).ljust(2,'0')
    return int(str(h) + s1 + s2)
  hours = list(filter(lambda x: x % 10 < 6, range(24)))
  minutes = list(range(0,56,11))
  seconds = list(map(lambda x: int(str(x)[::-1]),hours))
  count = 0
  for hour,second in zip(hours,seconds):
    if hour >= lst[0] and hour <= lst[3]:
      for minute in minutes:
        if string(hour,minute,second) >= string(lst[0],lst[1],lst[2]):
          if string(hour,minute,second) <= string(lst[3],lst[4],lst[5]):
            count += 1
​
  return count

