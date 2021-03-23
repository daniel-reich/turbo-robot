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
  while True:
    n += 1
    num_set = set()
    for num in str(n):
        num_set.add(num)
    if len(num_set) == 2:
        return n

