"""


Create a function that takes an integer argument and returns a list of prime
numbers found in the decimal representation of that number (not factors).

For example, `extract_primes(1717)` returns `[7, 7, 17, 17, 71]`.

The list should be in acending order. If a prime number appears more than
once, every occurance should be listed. If no prime numbers are found, return
an empty list.

### Examples

    extract_primes(1) ➞ []
    
    extract_primes(7) ➞ [7]
    
    extract_primes(73) ➞ [3, 7, 73]
    
    extract_primes(103) ➞ [3]
    
    extract_primes(1313) ➞ [3, 3, 13, 13, 31, 131, 313]

### Notes

  * All test cases are positive real integers.
  * Some numbers will have leading zeros. For example, the number `103` contains the prime number `3`, but also contains `03`. These should be treated as the same number, so the result would simply be `[3]`.

"""

def isPrime(n):
    import math
    if n <= 1: return False
    numbers_to_check = range(2,math.floor(math.sqrt(n))+1)
    for e in numbers_to_check:
        if n % e == 0:
            return False
    return True
​
def extract_primes(n):
    l = []
    for length in range(1,len(str(n))+1):
        for idx in range(len(str(n))-length+1):
            t = int(str(n)[idx:idx+length])
            if len(str(t)) != length:
                continue
            if isPrime(t):
                l.append(t)
    return sorted(l)

