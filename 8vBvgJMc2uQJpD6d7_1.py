"""


Create a function that returns a list containing the prime factors of whatever
integer is passed to it.

### Examples

    prime_factors(20) ➞ [2, 2, 5]
    
    prime_factors(100) ➞ [2, 2, 5, 5]
    
    prime_factors(8912234) ➞ [2, 47, 94811]

### Notes

  * Implement your solution using trial division.
  * Your solution should not require recursion.

"""

def prime_factors(n):
    res = []
    for i in range(2, int(n**0.5) + 1): 
        while not n%i: 
            res.append(i) 
            n //= i
    return res + [n] if n > 1 else res

