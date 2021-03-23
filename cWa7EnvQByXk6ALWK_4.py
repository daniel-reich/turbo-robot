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
  it = 100
  it, root5, n = 100, 0, 5
  a, d = 2, 2
  for _ in range(100):
      root5 = 10 * root5 + d
      n = (n - a * d) * 100
      a = root5 * 20
      d = n // a
      if (a + d + 1) * (d + 1) <= n:
          d += 1
      a += d
  return "1.6" + str(root5 // 2)[2:]

