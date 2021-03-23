"""


Create a function that takes a number and returns one digit that is the result
of summing all the digits of the input number. When the sum of the digits
consists of more than one digit, repeat summing until you get one digit.

### Examples

    root_digit(123) ➞ 6
    # 1 + 2 + 3 = 6
    
    root_digit(999888777) ➞ 9
    
    root_digit(1238763636555555555555) ➞ 6

### Notes

Recursion is allowed.

"""

def root_digit(n):
  sum_digits = 0
  for i in str(n):
    sum_digits += int(i)
  if sum_digits > 9:
    return root_digit(sum_digits)
  return sum_digits

