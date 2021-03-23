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
 start=(["0"+str(i) if len(str(i))==1 else str(i) for i in lst[:3]])
 end=(["0"+str(i) if len(str(i))==1 else str(i) for i in lst[3:]])
 count=0
 for h in range(int(start[0]),int(end[0])+1):
  for m in range(00,60):
   for s in range(00,60):
     x="".join(str("%.2d"%h)+str("%.2d"%m)+str("%.2d"%s))
     if int("".join(start))<=int(x)<=int("".join(end)) and  x==x[::-1]:
      count+=1
​
 return count

