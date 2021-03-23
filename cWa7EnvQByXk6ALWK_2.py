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

import decimal
decimal.getcontext().prec = 100
​
def golden_ratio():
    n = decimal.Decimal(1)
    for _ in range(250):
        n = 1/n + 1
    return str(n)

