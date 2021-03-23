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

def probability(u):
  pnot = 1
  for i in range(u-1):
    pnot*= (364-i)/365
  return round(1 - pnot,2)

