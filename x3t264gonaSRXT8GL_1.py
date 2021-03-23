"""


Given an integer `n`, create a function that returns the length of the
repeating cycle of the sequence **1/n**. If the cycle is non-repetitive,
return `-1`.

    repeating_cycle(13) ➞ 6
    # 1/13 = 0.076923 076923 076923 076923 ...
    # length of `076923` is 6.

### Examples

    repeating_cycle(5) ➞ -1
    # 1/5 = 0.2 (non-repeative)
    
    repeating_cycle(33) ➞ 2
    # 1/33 = 0.03 03 03 03 03 03 03 03
    # length of `03` is 2
    
    repeating_cycle(197) ➞ 98

### Notes

Return `-1` if the repeating cycle does not start from the first decimal
place. As an example, 1/22 = 0.0 45 45 45 45, your function should return `-1`
in this case.

"""

def repeating_cycle(n):
    res, first = 0, 1 % n * 10
    remainder, set_rem = first, set()
    while remainder not in set_rem:
        set_rem.add(remainder)
        res += 1
        remainder %= n
        remainder *= 10
    return res if remainder == first else -1
