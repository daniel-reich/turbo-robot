"""
**Mubashir** needs your help to find out trailing zeros after calculating
factorial of a given number.

Create a function which takes a number `n` and calculates the **number of
trailing zeros** in factorial of the given number.

    n! = 1 * 2 * 3 * ... * n

### Examples

    trailing_zeros(0) ➞ 0
    # 0! = 1
    # No trailing zero.
    
    trailing_zeros(6) ➞ 1
    # 6! = 120
    # 1 trailing zero.
    
    trailing_zeros(1000) ➞ 249
    # 1000! has 249 trailing zeros.

### Notes

 **Hint:** No need to calculate the factorial (because it won't help). Find
another way to find the number of zeros.

"""

"""
1. No factorial is going to have fewer zeros than the factorial 
of a smaller number.
​
2. Each multiple of 5 adds a 0, so first we count how many multiples of 5 are
  smaller than `n` (`n // 5`).
​
3. Each multiple of 25 adds two 0's, so next we add another 0 for each 
  multiple of 25 smaller than n.
​
4. We continue on for all powers of 5 smaller than (or equal to) n.
"""
def trailing_zeros(n):
    pow_of_5 = 5
    zeros = 0
    
    while n >= pow_of_5:
        zeros += n // pow_of_5
        pow_of_5 *= 5
        
    return zeros

