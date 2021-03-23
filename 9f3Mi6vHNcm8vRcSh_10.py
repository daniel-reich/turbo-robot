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
    import math
    holding = []
    if n%2 == 0:
        a = int(n/2)
        holding.append(a)
        return holding*2
    else:
        b = math.floor(n/2)
        c = math.ceil(n/2)
        holding.append(b)
        holding.append(c)
        return holding

