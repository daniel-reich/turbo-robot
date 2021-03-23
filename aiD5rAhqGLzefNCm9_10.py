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

def is_prime(num):
  nbin = bin(num-1)[2:][::-1]
  for i in [2,3,5,7,11,13,17,19,23,29]:
    power = i
    test = 1
    for k in range(len(nbin)):
      test = test*power % num if int(nbin[k])==1 else test
      power = power**2 %num
    if test!=1: return False
  return True

