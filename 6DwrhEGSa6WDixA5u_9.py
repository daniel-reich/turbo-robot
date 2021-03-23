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
  return sum([int(i)**len(str(n)) for i in str(n)])==n

