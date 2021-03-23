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

def prime_factorization(n):
    res = []
    for i in range(2, int(n**0.5) + 1): 
        while not n%i: 
            res.append(i) 
            n //= i
    return res + [n] if n > 1 else res
​
def sum_prime(lst):
    groups = [(i, set(prime_factorization(i))) for i in lst]
    res = {}
    for n, factors in groups:
        for f in factors:
            if f in res:
                res[f] += n
            else:
                res[f] = n
    return ''.join('({} {})'.format(k, v) for k, v in sorted(res.items()))

