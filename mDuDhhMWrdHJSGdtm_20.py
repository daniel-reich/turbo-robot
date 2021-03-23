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

def is_exactly_three(n):
    sqrt = round(n**(1/2))
    return sqrt >= 2 and sqrt**2 == n and all(n % i for i in range(2,sqrt//2+1))

