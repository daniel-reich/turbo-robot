"""


Create a function that will return an integer number containing the amount of
digits in the given integer `num`.

### Examples

    num_of_digits(1000) ➞ 4
    
    num_of_digits(12) ➞ 2
    
    num_of_digits(1305981031) ➞ 10
    
    num_of_digits(0) ➞ 1

### Notes

Try to solve this challenge without using strings!

"""

def num_of_digits(num):
  if num == 0:
    return 1
  count = 0
  num = abs(num)
  while (num > 0):
    num = num//10
    count += 1
  return count

