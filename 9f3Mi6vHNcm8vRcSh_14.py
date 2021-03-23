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
  if n%2 == 0 :
    return [n/2 , n/2]
  if n%2 == 1 and n>0:
    return [int(n/2) , int(n/2)+1 ]
    
  if n%2 == 1 and n<0:
    return [int(n/2)-1 , int(n/2) ]

