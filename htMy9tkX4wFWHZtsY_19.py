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
   a=[];k=0
   s1 = str(lst[0]) + ':' + str(lst[1]) +':' + str(lst[2])
   s2 = str(lst[3]) + ':' + str(lst[4]) + ':' + str(lst[5])
   FMT = '%H:%M:%S'
   t1 = datetime.strptime(s1, FMT)
   t2 =  datetime.strptime(s2, FMT)
   while t1<=t2:
     a.append(str(t1)[11:13]+str(t1)[14:16]+str(t1)[17:19])
     t1 = t1 + timedelta(0, 1)
   for i in a:
       if i==i[:-9:-1]:
          k=k+1
   return (k)

