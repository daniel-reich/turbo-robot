"""


Create a function that takes a list of `resistors` and calculates the output
of total resistance if the circuit is connected in **parallel** or in
**series**.

### Examples

    resistance_calculator([10, 20, 30, 40, 50]) ➞ [4.38, 150]
    
    resistance_calculator([25, 14, 65, 18]) ➞ [5.48, 122]
    
    resistance_calculator([10, 10]) ➞ [5, 20]
    
    resistance_calculator([0, 0, 0, 0]) ➞ [0, 0]
    
    resistance_calculator([1.1, 2.1, 3.2, 4.3, 5.4, 6.5]) ➞ [0.44, 22.6]

### Notes

  * Return parallel resistance as the first element and series resistance as second element of the list.
  * Round up the total resistance to two decimal places.

"""

from functools import reduce
def resistance_calculator(resistors):
  if any(r == 0 for r in resistors):
    return [0, round(sum(resistors), 2)]
  tot = reduce(lambda a,r: [a[0] + 1/r, a[1] + r], resistors, [0, 0])
  return [round(1/tot[0], 2), round(tot[1], 2)]

