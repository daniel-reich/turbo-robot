"""


A left-truncatable prime is a prime number that contains no 0 digits and, when
the first digit is successively removed, the result is always prime.

A right-truncatable prime is a prime number that contains no 0 digits and,
when the last digit is successively removed, the result is always prime.

Create a function that takes an integer as an argument and:

  * If the integer is only a left-truncatable prime, return `"left"`.
  * If the integer is only a right-truncatable prime, return `"right"`.
  * If the integer is both, return `"both"`.
  * Otherwise, return `False`.

### Examples

    truncatable(9137) ➞ "left"
    # Because 9137, 137, 37 and 7 are all prime.
    
    truncatable(5939) ➞ "right"
    # Because 5939, 593, 59 and 5 are all prime.
    
    truncatable(317) ➞ "both"
    # Because 317, 17 and 7 are all prime and 317, 31 and 3 are all prime.
    
    truncatable(5) ➞ "both"
    # The trivial case of single-digit primes is treated as truncatable from both directions.
    
    truncatable(139) ➞ False
    # 1 and 9 are non-prime, so 139 cannot be truncatable from either direction.
    
    truncatable(103) ➞ False
    # Because it contains a 0 digit (even though 103 and 3 are primes).

### Notes

The input integers will not exceed 10^6.

"""

def isprime(a):
    if a == 1:
        return False
    for i in range(2, int((a**0.5) + 1)):
        if a % i == 0:
            return False
    return True
​
​
def truncatable(n):
    s = str(n)
    if "0" in s:
        return False
    l, r = True, True
    x, y = s, s
    for i in range(len(s)):
        if not isprime(int(x)):
            l = False
        x = x[1:]
        if not isprime(int(y)):
            r = False
        y = y[:-1]
    if r == True and l == True or len(s) == 1:
        return "both"
    elif r == True:
        return "right"
    elif l == True:
        return "left"
    else:
        return False

