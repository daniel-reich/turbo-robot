"""


Given a number, return all its prime divisors in a list. Create a function
that takes a number as an argument and returns all its prime divisors.

  * n = 27
  * All divisors: `[3, 9, 27]`
  * Finally, from that list of divisors, return the prime ones: `[3]`

### Examples

    prime_divisors(27) ➞ [3]
    
    prime_divisors(99) ➞ [3, 11]
    
    prime_divisors(3457) ➞ [3457]

### Notes

N/A

"""

def prime_divisors(num):
    res = set()
    while not num % 2:
        num //= 2
        res.add(2)
    divisor = 3
    while num > 1:
        while not num % divisor:
            num //= divisor
            res.add(divisor)
        divisor += 2
    """1 is not a prime factor but author put it into the tests"""
    res.add(1)
    return sorted(res)

