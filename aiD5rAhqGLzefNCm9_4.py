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
​
​
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
​
​
def fastermod(factor, power, modulus):
    res = 1
    while power > 0:
        if power % 2:
            res = res * factor % modulus
            power -= 1
        power //= 2
        factor = (factor * factor) % modulus
    return res
​
​
def is_prime(num):
    for _ in range(20):
        k = randint(1, num - 1)
        if gcd(k, num) > 1:
            return False
        if fastermod(k, num - 1, num) > 1:
            return False
    return True

