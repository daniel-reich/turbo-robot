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

def prime_divisors(x):
    factors1 = []
    i = 2
    while x > 1:
        if x % i == 0:
            x = x / i
            factors1.append(i)
        else:
            i += 1
    factors2 = [i for i in factors1 if all(i % x for x in range(2, i))]
    res = []
    for i in factors2:
        if i not in res:
            res.append(i)
    return res

