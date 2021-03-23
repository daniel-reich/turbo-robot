"""


Create a function that takes a number `n` as an argument and checks whether
the given number can be expressed as a sum of **two or more consecutive
positive numbers**.

### Examples

    consecutiveSum(9) ➞ True
    # 9 can be expressed as a sum of (2 + 3 + 4) or (4 + 5).
    
    consecutiveSum(10) ➞ True
    # 10 can be expressed as a sum of 1 + 2 + 3 + 4.
    
    consecutiveSum(64) ➞ False

### Notes

N/A

"""

def consecutive_sum(n):
    n2 = 2 * n
    for diff in range(1, n + 1):
        if not n2 % (diff + 1):
            start2 = n2 // (diff + 1) - diff
            if not start2 % 2 and 0 < start2 // 2 < n:
                return True
    return False

