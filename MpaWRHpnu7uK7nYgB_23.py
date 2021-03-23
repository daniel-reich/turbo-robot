"""


 **Mubashir** was reading about [Doubleton
Numbers](https://proofwiki.org/wiki/Definition:Doubleton) on Wikipedia.

A natural number is a **"Doubleton Number"** , if it contains _exactly two
distinct digits_. For example, 23, 35, 100, 12121 are doubleton numbers, and
123 and 114455 are not.

Create a function which takes a number `n` and finds the **next doubleton
number**.

### Examples

    doubleton(10) ➞ 12
    # 12 has only two distinct numbers 1 and 2
    
    doubleton(120) ➞ 121
    # 121 has only two distinct numbers 1 and 2
    
    doubleton(1234) ➞ 1311
    # 1311 has only two distinct numbers 1 and 3

### Notes

N/A

"""

def doubleton(n):
  n, c = n + 1, 0
  while c < 1:
    x, y, lst = n, 0, []
    while x:
      if x % 10 not in lst:
        lst += [x % 10]
        y += 1
      x //= 10
    if y == 2:
      c += 1
    else:
      n += 1
  return n

