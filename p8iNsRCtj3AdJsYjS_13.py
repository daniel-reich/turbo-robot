"""
Given a column title as it appears in an Excel sheet return its corresponding
column number.

The number is computed in the following way:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

### Examples

    title_to_number("A") ➞ 1
    
    title_to_number("R") ➞ 18
    
    title_to_number("AB") ➞ 28

### Notes

  * `1 <= len(s) <= 7`
  * `s` consists only of uppercase English letters.

"""

import functools
def title_to_number(s):
  def convert(string):
    list1 = []
    list1[:0] = string
    return list1
  rev = list(reversed(convert(s)))
  i = 0
  while i < len(rev):
    rev[i] = (ord(rev[i]) - 64) * 26 ** i
    i += 1
  return functools.reduce(lambda a, b: a + b, rev)

