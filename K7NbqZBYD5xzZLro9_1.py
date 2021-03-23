"""


Create a function that takes a range of numbers and returns the sum of each
digit from `start` to `stop`.

### Examples

    digits_sum(1, 10) ➞ 46
    # total numbers in the range are = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    # sum of each digits is = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 1 + 0 = 46
    
    digits_sum(1, 20) ➞ 102
    
    digits_sum(1, 100) ➞ 901

### Notes

`start` and `stop` are inclusive in the range.

"""

from math import log10
def digits_sum(start, stop):
    res = 0
    if stop < 1000:
        for i in range(start, stop + 1):
            res += sum(int(c) for c in str(i))
    else:
        n = int(log10(stop))
        total = 45 * pow(10, n - 1) * n
        before = 0
        for i in range(start):
            before += sum(int(c) for c in str(i))
        res = total + 1 - before
    return res

