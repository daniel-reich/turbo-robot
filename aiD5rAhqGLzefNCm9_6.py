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

from random import randrange
def is_prime(n):
  if n in (0,1,4,6,8,9): return False
  if n in (2,3,5,7): return True
  s, d = 0, n-1
  while not d%2:
    d >>= 1
    s += 1
  for i in range(8):
    a = randrange(2, n)
    if test_composite(a, d, n, s): return False
  return True
​
def test_composite(a, d, n, s):
  if pow(a, d, n) == 1: return False
  for i in range(s):
    if pow(a, 2**i * d, n) == n-1: return False
  return True

