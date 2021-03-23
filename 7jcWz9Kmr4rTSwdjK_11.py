"""


Write a function to find all the prime factors of a given integer. The
function must return a list containing all the prime factors, sorted in
ascending order. Remember that _1 is neither prime nor composite_ and should
not be included in your output list.

### Examples

    prime_factorize(25) ➞ [5, 5]
    
    prime_factorize(19) ➞ [19]
    
    prime_factorize(77) ➞ [7, 11]

### Notes

  * Output list must be sorted in ascending order.
  * The only positive integer which is neither prime nor composite is 1. Return an empty list if 1 is the input.

"""

def has_factors(n):
    if abs(n) < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return True
    return False
​
def prime_factorize(n):
    if n < 2:
        return []
    factors = []
    if not has_factors(n):
        factors.append(n)
    while has_factors(n):
        for i in range(2, n):
            if n % i == 0:
                if not has_factors(i):
                    factors.append(i)
                    n = n // i
        if n != 1 and not has_factors(n):
            factors.append(n)
    factors.sort()
    return factors

