"""


Two consecutive integers `a` and `b` are considered a **Ruth-Aaron pair** if
the sum of the prime factors of `a` is equal to the sum of the prime factors
of `b`.

Two definitions exist:

  1. Summing up _distinct_ prime factors. For example, 24 and 25 constitute a Ruth-Aaron pair by this definition. 8 and 9 do not.

    P24 = [2, 3]  # sum = 5
    
    P25 = [5]  # sum = 5, equal to 24
    
    P8 = [2]  # sum = 2
    
    P9 = [3]  # sum = 3

  2. Summing up _repeated_ prime factors. By this definition, 24 and 25 do _not_ constitute a Ruth-Aaron pair. But 8 and 9 do.

    P24 = [2, 2, 2, 3]  # sum = 9
    
    P25 = [5, 5]  # sum = 10
    
    P8 = [2, 2, 2]  # sum = 6
    
    P9 = [3, 3]  # sum = 6, equal to 8

If two consecutive numbers have only distinct prime factors and have equal
sums of prime factors, they are considered Ruth-Aaron pairs by both
definitions.

    P77 = [7, 11]  # sum = 18
    
    P78 = [2, 3, 13]  # sum = 18

Create a function that takes a number `n` and returns:

  1. `False` if it is not part of a Ruth-Aaron pair.
  2. A 2-element list if it is part of a Ruth-Aaron pair.
    * The first element should be "Ruth" if `n` is the smaller number in the pair, or "Aaron" if it is the larger.
    * The second element should be 1 if `n` is part of a Ruth-Aaron pair under the first definition (sum of _distinct_ prime factors), 2 if it qualifies by the second definition, 3 if it qualifies under both.

### Examples

    ruth_aaron(5) ➞ ["Ruth", 3]
    
    ruth_aaron(25) ➞ ["Aaron", 1]
    
    ruth_aaron(9) ➞ ["Aaron", 2]
    
    ruth_aaron(11) ➞ False

### Notes

N/A

"""

def get_prime_factors(n):
    f = 2
    factors = []
    limit = n // 2
    while f <= limit:
        if n % f == 0:
            factors.append(f)
            n /= f
        else:
            f += 1
    if f > limit and not factors: factors.append(n)
    return factors
​
​
def get_sum_type(a, b):
    a_f = get_prime_factors(a)
    b_f = get_prime_factors(b)
​
    if sum(a_f) == sum(b_f):
        if len(a_f) == len(set(a_f)) and len(b_f) == len(set(b_f)):
            return 3
        else:
            return 2
    elif sum(set(a_f)) == sum(set(b_f)):
        return 1
    else:
        return False
​
​
def ruth_aaron(n):
    for n_pair in [n - 1, n + 1]:
        sum_type = get_sum_type(n, n_pair)
        if sum_type:
            pair_type = 'Ruth' if n < n_pair else 'Aaron'
            return [pair_type, sum_type]
    return False

