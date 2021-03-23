"""


Every number can be expressed as the sum between unique powers of two. For
example, the number `21` can be expressed as `1 + 4 + 16`, which can also be
written as `2^0 + 2^2 + 2^4`.

Create a function that returns a sorted list of powers of two, which add
together to make `n`.

### Examples

    sums_of_powers_of_two(21) ➞ [1, 4, 16]
    
    sums_of_powers_of_two(8) ➞ [8]
    
    sums_of_powers_of_two(63) ➞ [1, 2, 4, 8, 16, 32]

### Notes

Tests will only include positive whole numbers.

"""

def sums_of_powers_of_two(n):
    b = bin(n)[2:][::-1]
    p = 1
    ans = []
    for bit in b:
        if bit == '1':
            ans.append(p)
        p *= 2
    return ans

