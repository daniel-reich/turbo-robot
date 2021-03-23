"""


A positive integer multiplied times its inverse is always equal to 1:
`17*(1/17)==1`. Modular arithmetic has a similar inverse function, although,
for modulus `m`, we are confined to integers from 0 to m-1. The modular
multiplicative inverse of 3 modulus 5 is equal to 2 because `(3*2)%5==1`.
Another example: the modular inverse of 17 modulus 1000007 is equal to 58824
because `(17*58824)%1000007==1`. The modular inverse, if it exists, must
always be in the range 0 to m-1.

Create a function that has arguments integer `n` and modulus `m`. The function
will return the modular inverse of `n` mod `m`. If the modular inverse does
not exist, return `False`.

### Examples

    mod_inv(2, 3) ➞ 2
    
    mod_inv(12, 47) ➞ 4
    
    mod_inv(11, 33) ➞ False
    
    mod_inv(55, 678) ➞ 37
    
    mod_inv(81, 3455) ➞ 2346

### Notes

  * Some of the test cases have rather large integers, so if you attempt to do a brute force search of the entire modular field, you may not be successful due to the 12 second time limit imposed by the server. See **Resources** for a more efficient approach.
  * The modular inverse of a number `n` modulus `m` exists only if `n` and `m` are coprime (i.e. they have no common factors other than 1).
  * One practical use of modular inverse is in public-key cryptography like RSA where it can be used to determine the value of the private key.

"""

def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if not n % 2:
        return False
    for k in range(3, int(n ** 0.5) + 1, 2):
        if not n % k:
            return False
    return True
​
​
def prime_factors(num):
    res = []
    while not num % 2:
        num //= 2
        res += [2]
    divisor = 3
    while num > 1:
        while not num % divisor:
            num //= divisor
            res += [divisor]
        divisor += 2
    return res
​
​
def mod_inv(n, m):
    n_factors, m_factors = prime_factors(n), prime_factors(m)
    for i in n_factors:
        if i in m_factors:
            return False
    if is_prime(m):
        base = n
        power = m - 2
        mod = m
        result = 1
        while power > 0:
            if power % 2 == 1:
                result = (result * base) % mod
            power = power // 2
            base = (base * base) % mod
    else:
        s, old_s = 0, 1
        t, old_t = 1, 0
        r, old_r = m, n
        while r != 0:
            quotient = old_r // r
            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s
            old_t, t = t, old_t - quotient * t
        result = old_s
        if result < 0:
            result += m
    return result

