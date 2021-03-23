"""


A number is narcissistic when the sum of its digits, with each digit raised to
the power of digits quantity, is equal to the number itself.

    153 ➞ 3 digits ➞ 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 ➞ Narcissistic
    84 ➞ 2 digits ➞ 8² + 4² = 64 + 16 = 80 ➞ Not narcissistic

Given a positive integer `n`, implement a function that returns `True` if the
number is narcissistic, and `False` if it's not.

### Examples

    is_narcissistic(8208) ➞ True
    // 8⁴ + 2⁴ + 0⁴ + 8⁴ = 8208
    
    is_narcissistic(22) ➞ False
    // 2² + 2² = 8
    
    is_narcissistic(9) ➞ True
    // 9¹ = 9

### Notes

  * Trivially, any number in the 1-9 range is narcissistic and any two-digit number is not.
  * Curious fact: Only 88 numbers are narcissistic.

"""

def is_narcissistic(n):
  total = 0
  num_str = str(n)
  power_exp = len(num_str)
  num_lst = []
  for num in num_str:
    exp = int(num) ** power_exp 
    num_lst.append(exp)
  
  for i in range(len(num_lst)):
    total += num_lst[i]
  
  if n == total:
    return True
  else:
    return False

