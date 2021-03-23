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

from datetime import datetime,timedelta
def palindrome_time(lst):
  a,b,c,x,y,z = [str(i) for i in lst]
  palin = []
  start = datetime.strptime(a+':'+b+':'+c,'%H:%M:%S')
  end = datetime.strptime(x+':'+y+':'+z,'%H:%M:%S')
  while start<=end:
    temp=start.strftime("%H:%M:%S")
    if is_pal(temp):
      palin.append(temp)
    start+=timedelta(seconds=1)
  return len(palin)
  
def is_pal(s):
  return s==s[::-1]

