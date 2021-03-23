"""


Create a function that takes a list of positive integers and returns a string
as:

  *  **p1** , **sum of all ij** of the list for which **p1** is a prime factor.
  *  **p2** , **sum of all ij** of the list for which **p2** is a prime factor, **...** .
  *  **pn** , **sum of all ij** of the list for which **pn** is a prime factor.

### Examples

    sum_prime([12, 15]) ➞ "(2 12)(3 27)(5 15)"
    # 2 is a prime factor of 12 results (2 12).
    # 3 is a prime factor of 12 and 15, add 15 + 12, results (3 27).
    # 5 is a prime factor of 15 results (5 15).
    # 7, 11 and 13 are prime numbers but not a factor of any of the number
    # in the given list.
    
    sum_prime([7, 13, 18, 23, 24]) ➞ "(2 42)(3 42)(7 7)(13 13)(23 23)"
    
    sum_prime([3, 5, 7, 9, 11, 13]) ➞ "(3 12)(5 5)(7 7)(11 11)(13 13)"

### Notes

N/A

"""

def gen_primes(n):
    primes = {2}
    for k in range(3, n, 2):
        if all(k % p > 0 for p in primes):
            primes.add(k)
    return sorted(primes)
​
lst_p = gen_primes(224)
​
def sum_prime(lst):
    res = ''
    for p in lst_p:
        if p > lst[-1]:
            break
        s = sum(n for n in lst if not n % p)
        if s > 0:
            res += '({} {})'.format(p, s)
    return res

