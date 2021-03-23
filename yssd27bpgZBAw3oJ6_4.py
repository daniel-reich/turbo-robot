"""


Create a function that takes the number of people `u` in a room and calculates
the probability that any two people in the room share the same birthday. Round
the result to two decimal places.

### Examples

    probability(7) ➞ 0.06
    
    probability(15) ➞ 0.25
    
    probability(12) ➞ 0.17

### Notes

  * u < 40
  * 1 year = 365 days not 366

"""

def probability(u, rounding=True):
  if u > 365:
    return 1
  if u == 2:
    return 1 / 365
  out = 1 - (1 - probability(u - 1, False)) * (366 - u) / 365
  if rounding:
    return round(out, 2)
  return out

