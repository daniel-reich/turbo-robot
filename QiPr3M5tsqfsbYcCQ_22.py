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
  temp=n
  s=''
  sq=0
  while temp>0:
    dig=temp%10
    sq=dig**2
    temp=temp//10
    s=str(sq)+s
  return int(s)

