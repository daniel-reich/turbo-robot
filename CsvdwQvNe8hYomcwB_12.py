"""


Create a function similar to Processings "map" function (check the
**Resources** tab), in which a value and its range is taken and remapped to a
new range.

The function takes 5 numbers:

  * Value: `value`
  * Range: `low1` and `high1`
  * Range: `low2` and `high2`

### Examples

    remap(7, 2, 12, 0, 100) ➞ 50
    
    remap(17, 5, 55, 100, 30) ➞ 83.2
    
    remap(50, 1, 51, 0, 100) ➞ 98

### Notes

  * Test input will always be numbers.
  * If the input range is `0`, return `0`.

"""

def remap(value, low1, high1, low2, high2):
  try: ratio = (value - low1) / (high1 - low1)
  except: return 0
  return low2 + (high2 - low2) * ratio

