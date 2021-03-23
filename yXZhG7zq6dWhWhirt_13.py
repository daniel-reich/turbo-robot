"""


Create a function that takes a list and returns a new list containing only
prime numbers.

### Examples

    filter_primes([7, 9, 3, 9, 10, 11, 27]) ➞ [7, 3, 11]
    
    filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70]) ➞ [10007, 1009]
    
    filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]) ➞ [1009, 3, 61, 1087, 1091, 1093, 1097]

### Notes

  * New list must maintain the order of primes as they first appear in the original list.
  * Check the **Resources** tab for help.

"""

def filter_primes(num):
    
    def is_prime(n):
        p = []
        for i in range(1, n + 1):
            if n % i == 0:
                p.append(i)
        if len(p) == 2:
            return True
        else:
            return False
        
    primes = []
    for i in num:
        if is_prime(i):
            primes.append(i)
    return primes

