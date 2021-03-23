"""


Given an number, return a string which contains varying amounts of the word
`'MEGA'` depending on the given number's order of magnitude.

  * If the number is less than 100, return `"not a mega milestone"`.
  * Otherwise, start with the string `"MEGA milestone"`.
  * For every order of magnitude over 100 that the number is, add the word `"MEGA"` to the _start_ of the string.

See the examples below for further clarification!

### Examples

    how_mega_is_it(54) ➞ "not a mega milestone"
    
    how_mega_is_it(143) ➞ "MEGA milestone"
    
    how_mega_is_it(1000) ➞ "MEGA MEGA milestone"
    
    how_mega_is_it(9999.9) ➞ "MEGA MEGA milestone"
    
    how_mega_is_it(10000) ➞ "MEGA MEGA MEGA milestone"

### Notes

  * Large negative numbers can also be considered as MEGA, so use the absolute values.
  * You can expect decimal numbers as well as whole numbers.

"""

def how_mega_is_it(n):
  a = abs(n)
  if a < 100:
    return "not a mega milestone"
  else:
    import math
    return (len(str(math.floor(a)))-2) * "MEGA " + "milestone"

