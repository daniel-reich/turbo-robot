"""


Given two integers as arguments, create a function that finds the largest
prime within the range of the two integers.

### Examples

    fat_prime(2, 10) ➞ 7
    # range [2, 3, 4, 5, 6, 7, 8, 9, 10] and the largest prime is 7.
    
    fat_prime(10, 2) ➞ 7
    # [10, 9, 8, 7, 6, 5, 4, 3, 2] and the largest prime is 7.
    
    fat_prime(4, 24) ➞ 23
    # range [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24] the largest prime is 23.

### Notes

All numbers will be positive integers.

"""

def fat_prime(a, b):
  def is_prime(num):
    if num <= 1:
      return False
    for n in range(2, num):
      if num % n == 0:
        return False
    return True
  
  if b < a:
    a, b = b, a
  while is_prime(b) == False:
    b -= 1
  
  return b

