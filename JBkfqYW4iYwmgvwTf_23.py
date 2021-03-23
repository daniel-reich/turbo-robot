"""


Create a function that returns `True` if a number is prime, and `False`
otherwise. A prime number is any positive integer that is evenly divisible by
only two divisors: 1 and itself.

The first ten prime numbers are:

    2, 3, 5, 7, 11, 13, 17, 19, 23, 29

### Examples

    is_prime(31) ➞ True
    
    is_prime(18) ➞ False
    
    is_prime(11) ➞ True

### Notes

  * A prime number has no other factors except 1 and itself.
  * If a number is odd it is not divisible by an even number.
  * 1 is not considered a prime number.

"""

def is_prime(num):
  return num > 1 and not any(True for x in range(2, num // 2) if num % x == 0)

