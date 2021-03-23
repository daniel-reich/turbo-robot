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

def is_prime(num):
    if num == 2: return True
    sol, base, binary = 1, 2, str(bin(num - 1))[3:][::-1]
    for i in binary:
        if i == "1":
            sol = (sol*base) % num
        base = (base*base) % num
    return (sol*base) % num == 1
​
def is_exactly_three(n):
    return is_prime(int(n**0.5)) if n**0.5 == int(n**0.5) else False

