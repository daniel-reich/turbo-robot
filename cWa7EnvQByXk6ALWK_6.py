"""


The golden ratio is ubiquitous in math, science, art, and nature. This
challenge is concerned with the number itself, which is 1.618033988 to 10
significant digits. Implement a function that calculates the golden ratio to
100 significant digits using only integers, strings and basic arithmetic
operations: `+`, `-`, `*`, `//`

### Examples

    golden_ratio() ➞ 1.618033988+90 more decimal places

### Notes

This function has no argument so naturally there is only one test case.

"""

def mid(l, h, half, sq, n):
    return [half, h] if sq < n else [l, half]
​
def square_root(n):
    [l, h] = [0, n]
    while True:
        half = (l+h)//2; sq = half*half
        if h-l < 2: return half
        l, h = mid(l, h, half, sq, n)
​
def golden_ratio():
    return "1.6"+str(square_root(125*10**196))[2:]

