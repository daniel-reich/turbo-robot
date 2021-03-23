"""


Create a function that squares every digit of a number.

### Examples

    square_digits(9119) ➞ 811181
    
    square_digits(2483) ➞ 416649
    
    square_digits(3212) ➞ 9414

### Notes

The function receives an integer and must return an integer.

"""

def square_digits(n):
  s = str(n)
  ar = [str(int(d)**2) for d in s]
  s = ''.join(ar)
  return int(s)

