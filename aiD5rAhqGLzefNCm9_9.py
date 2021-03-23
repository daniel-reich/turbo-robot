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
def is_prime(n): 
    k = 5
    
    if n < 2: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n % p == 0: return n == p
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d//2
    for i in range(k):
        x = pow(randint(2, n-1), d, n)
        if x == 1 or x == n-1: continue
        for r in range(1, s):
            x = (x * x) % n
            if x == 1: return False
            if x == n-1: break
        else: return False
    return True

