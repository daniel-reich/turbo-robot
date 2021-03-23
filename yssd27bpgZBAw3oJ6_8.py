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
    ss = 365**u
    distinctbd = 1
    count = 0
    for days in range(365, 325, -1):
        if count == u:
            break
        distinctbd *= days
        count += 1
    prob = 1 - (distinctbd/ss)
    return round(prob,2)

