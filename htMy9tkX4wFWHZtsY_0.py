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

s_pals = [0,10,20,30,40,50,1,11,21,31,41,51,2,12,22,32]
m_pals = [0,11,22,33,44,55]
h_pals = [0,1,2,3,4,5,10,11,12,13,14,15,20,21,22,23]
pals = [[h,m,s] for m in m_pals for s,h in zip(s_pals,h_pals)]
​
def palindrome_time(lst):
  s1,m1,h1,s2,m2,h2 = lst
  
  return sum(1 for p in pals if p<=[s2,m2,h2])-\
          sum(1 for p in pals if p<[s1,m1,h1])

