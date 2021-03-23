"""


Create a function that decomposes an integer into its prime factors, ordered
from smallest to largest.

For instance:

    complete_factorization(24) = [2, 2, 2, 3]
    # Since 24 = 8 x 3 = 2^3 x 3 = 2 x 2 x 2 x 3

### Examples

    complete_factorization(10) ➞ [2, 5]
    
    complete_factorization(9) ➞ [3, 3]
    
    complete_factorization(72) ➞ [2, 2, 2, 3, 3]

### Notes

`1` is not considered a prime number, so omit it in your final list of prime
factors.

"""

def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if not n % 2:
        return False
    for k in range(3, int(n ** 0.5) + 1, 2):
        if n % k == 0:
            return False
    return True
​
​
def complete_factorization(num):
    if is_prime(num) or num == 1:
        return [num]
    prime_nums = [2]
    for i in range(3, num // 2 + 1, 2):
        if is_prime(i):
            prime_nums += [i]
    prime_nums = prime_nums[::-1]
    factors = []
    x = prime_nums.pop()
    while num > 1:
        if not num % x:
            num /= x
            factors += [x]
        else:
            x = prime_nums.pop()
    return factors

