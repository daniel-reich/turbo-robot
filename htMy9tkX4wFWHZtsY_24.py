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
  count = 0
  for t in range(lst[0]*3600 + lst[1]*60 + lst[2], lst[3]*3600 + lst[4]*60 + lst[5] + 1):
    txt = ("{:02d}" * 3).format(t // 3600, t // 60 % 60, t % 60)
    if txt == txt[::-1]:
      count += 1
  return count

