"""


Make a function that returns `True` if an integer is prime or `False` if the
number is composite. All test cases are of very large numbers, so **trial
division won't cut it**.

### Examples

    is_prime(308860934436978480666476812207644303437) ➞ True
    # The only factors for this number are 1 and itself.
    
    is_prime(27464981106643782905056206820270083251) ➞ False
    # This equals 13803066116705972713 * 1989773929533140027
    
    is_prime(12930519935023769075526485657382658729) ➞ False
    # This is 3595903215469483277 squared

### Notes

See the **Resources** tab for some great explanations of how computers can
find very large prime numbers for cryptography applications.

"""

from random import randint
def is_prime(num): 
  if num < 2: 
    return False
  for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 
              47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 
              107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 
              167, 173, 179, 181, 191, 193, 197, 199,]:
    if num % p == 0: 
      return False
  rrange, bbreak = 0, num-1
  while bbreak % 2 == 0:
    rrange, bbreak = rrange+1, bbreak//2
  for i in range(100):
    res = pow(randint(2, num-1), bbreak, num)
    if res == 1 or res == num-1:
      for i in range(1, rrange):
        res = res**2 % num
        if res == 1: 
          return False
        if res == num-1: 
          break
    else: return False
  return True

