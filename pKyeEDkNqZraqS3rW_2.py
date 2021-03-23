"""


Write a function that returns `True` if `k^k == n` for input `(n, k)` and
return `False` otherwise.

### Examples

    k_to_k(4, 2) ➞ True
    
    k_to_k(387420489, 9) ➞ True
    # 9^9 == 387420489
    
    k_to_k(3124, 5) ➞ False
    
    k_to_k(17, 3) ➞ False

### Notes

The `^` operator refers to exponentiation operation `**`, not the bitwise XOR
operation.

"""

k_to_k = lambda n, k: k**k == n;

