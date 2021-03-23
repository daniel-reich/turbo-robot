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
  prob_not = 1
  for person in range(2, u + 1):
    prob_not *= (364-(person - 2)) / 365
    
  return round(1 - prob_not, 2)

