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

def trailing_zeros(n):
  # https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/
    # Initialize result
    count = 0
 
    # Keep dividing n by
    # 5 & update Count
    while(n >= 5):
        n //= 5
        count += n
 
    return count

