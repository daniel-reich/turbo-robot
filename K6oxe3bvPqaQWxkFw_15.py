"""


Create a function which takes in a number `n` as input and returns all numbers
**up to and including n** joined together in a string. Separate each **digit
from each other** with the character `"-"`.

### Examples

    join_digits(4) ➞ "1-2-3-4"
    
    join_digits(11) ➞ "1-2-3-4-5-6-7-8-9-1-0-1-1"
    
    join_digits(15) ➞ "1-2-3-4-5-6-7-8-9-1-0-1-1-1-2-1-3-1-4-1-5"

### Notes

Remember to start at 1 and include `n` as the last number.

"""

def join_digits(n):
  c = ""
  for i in range(1,n+1):
    c+= str(i)
  return "-".join(c)

