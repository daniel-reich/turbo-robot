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

import math
​
def next_prime(n):
    n += 1
    is_prime = False
    i = 0
    while not is_prime:
        for j in range(2,math.floor(math.sqrt(n))+1):
            if n % j == 0:
                i += 1
        if i == 0:
            is_prime = True
        else:
            n += 1
            i = 0
    return n
​
def prime_factorize(n):
    prime_factors = []
    i = 2
    while n > 1:
        while n % i == 0:
            prime_factors += [i]
            n /= i
        i = next_prime(i)
    return prime_factors

