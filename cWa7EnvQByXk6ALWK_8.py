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

def golden_ratio():
  a,b = 1,10
  for i in range(400):
    a,b = b,a+b
  st = str((b*10**100)//a)
  return "1." + st[1:-1]

