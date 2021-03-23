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
    p_no_share = 1.
    for k in range(u):
        p_no_share *= (365 - k) / 365.
    return round(1. - p_no_share, 2)

