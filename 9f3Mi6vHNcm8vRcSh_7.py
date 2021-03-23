"""


Given a number, return a list containing the two halves of the number. If the
number is odd, make the **rightmost number higher**.

### Examples

    number_split(4) ➞ [2, 2]
    
    number_split(10) ➞ [5, 5]
    
    number_split(11) ➞ [5, 6]
    
    number_split(-9) ➞ [-5, -4]

### Notes

  * All numbers will be integers.
  * You can expect negative numbers too.

"""

def number_split(n):
  half=int(n/2)
  if half+half==n:
    return [half,half]
  if half>=0:
    half1=half+1
  else:
    half1=half-1
  a=[half,half1]
  if n>=0:
    return a
  else:
    return [min(half,half1),max(half,half1)]

