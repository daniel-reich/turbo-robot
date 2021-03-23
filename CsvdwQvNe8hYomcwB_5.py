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
  range1 = high1 - low1 
  if range1 == 0: return 0
  range2 = high2 - low2
  aux1 = (value - low1)/range1*range2 + low2
  return aux1

