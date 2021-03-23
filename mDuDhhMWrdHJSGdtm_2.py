"""


You are given a number `n`. Determine whether `n` has exactly **3 divisors**
or not.

### Examples

    is_exactly_three(4) ➞ True
    # 4 has only 3 divisors: 1, 2 and 4
    
    is_exactly_three(12) ➞ False
    # 12 has 6 divisors: 1, 2, 3, 4, 6, 12
    
    is_exactly_three(25) ➞ True
    # 25 has only 3 divisors: 1, 5, 25

### Notes

1 ≤ n ≤ 10^12

"""

def divisible(n):
    '''
    Returns True if n has exactly 3 divisors
    '''
    divisors = {1}
    divisors.add(n)  # every number has 1 & itself as a divisor
​
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            divisors.add(i)
            divisors.add(n // i)
            if len(divisors) > 3:
                return False
​
    return len(divisors) == 3

