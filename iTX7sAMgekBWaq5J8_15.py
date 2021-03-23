"""


Write a function that takes the last number of a consecutive list of numbers
and returns the total of all numbers up to and including it.

### Examples

    add_up_to(3) ➞ 6
    # 1 + 2 + 3 = 6
    
    add_up_to(10) ➞ 55
    # 1 + 2 + 3 + ... + 10 = 55
    
    add_up_to(7) ➞ 28
    # 1 + 2 + 3 + ... + 7 = 28

### Notes

  * You will only be given valid inputs.
  * There are two ways of doing this; try finding them both!
  * Remember to `return` the result.

"""

def add_up_to(n):
  sum1 = 0
  for i in range(n+1):
    sum1 = i + sum1
  return(sum1)

