"""


Given two integers `a` and `b`, return how many times `a` can be halved while
still being greater than `b`.

### Examples

    halve_count(4666, 544) ➞ 3
    # (4666 -> 2333 -> 1166.5 -> 583.25)
    
    halve_count(624, 8) ➞ 6
    # (624 -> 312 -> 156 -> 78 -> 39 -> 19.5 -> 9.75)
    
    halve_count(1000, 3) ➞ 8
    # (1000 -> 500 -> 250 -> 125 -> 62.5 -> 31.25 -> 15.625 -> 7.8125 -> 3.90625)

### Notes

  * Integer `a` will always be (at least) greater than the _twice_ of `b`.
  * You are expected to solve this challenge via a **recursive** approach.

"""

def halve_count(a, b):
  # recursive code here
  if a<=b:
    return -1
  else:
    return halve_count(a/2, b)+1

