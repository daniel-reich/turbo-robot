"""


Create a function that takes an array of strings of arbitrary dimensionality
(`[]`, `[][]`, `[][][]`, etc) and returns the deep_sum of every separate
number in each string in the array.

### Examples

    deep_sum(["1",  "five",  "2wenty",  "thr33"]) ➞ 36
    
    deep_sum([["1X2",  "t3n"], ["1024", "5", "64"]]) ➞ 1099
    
    deep_sum([[["1"], "10v3"],  ["738h"],  [["s0"],  ["1mu4ch3"], "-1s0"]]) ➞ 759

### Notes

  * Numbers in strings can be negative, but will all be base-10 integers.
  * Negative numbers may directly follow another number.
  * The hyphen or minus character ("-") does not only occur in numbers.
  * Arrays may be ragged or empty.

"""

import re
def flatten(lst):
  r = []
  for itm in lst:
    if isinstance(itm, list):
      r.extend(flatten(itm))
    else:
      r.append(itm)
  return r
​
def deep_sum(lst):
  s = 'X'.join(flatten(lst))
  nums = re.findall(r'-?\d+', s)
  return sum(int(n) for n in nums)

