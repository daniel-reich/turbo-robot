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
# Using Miller-Rabin primality test
def is_prime(n):
    k, t, d = 10, 0, n - 1
​
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
​
    while d%2 == 0:
        t += 1
        d //= 2
    for _ in range(k):
        a = randint(2, n - 1)
        res = pow(a, d, n)
        if res == 1:
            continue
        for _ in range(t - 1):
            if res == n - 1:
                break
            res = pow(res, 2, n)
        if res != n - 1:
            return False
    return True

