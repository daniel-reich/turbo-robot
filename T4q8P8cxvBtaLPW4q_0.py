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

def is_prime(p):
    return p > 1 and all(p%ii != 0 for ii in range(2, int(p**0.5 +1)))
​
def extract_primes(num):
    strnum = str(num)
    return sorted(int(strnum[start: start +size]) 
        for size in range(1, len(strnum) +1)
        for start in range(len(strnum) -size +1)
        if strnum[start] != '0' and is_prime(int(strnum[start: start +size])))

