"""


If two or more resistors are connected in parallel, the overall resistance of
the circuit reduces. It is possible to calculate the total resistance of a
parallel circuit by using this formula:

![1/RTotal = 1/R1 + 1/R2 + 1/R3 ...](https://edabit-
challenges.s3.amazonaws.com/VUqSzKSyFRpK7yA3MziSe7E67UIajN0A2RKrY5g0wEqGY_RkznFxqQwTTZykw9ua-
UXF-uzRRY92AjTPvj90V5Ln3T8ORk5fqh92.png)

Create a function that takes a list of resistance values, and calculates the
total resistance of the circuit.

### Worked Example

    parallel_resistance([6, 3, 6]) ➞ 1.5
    
    # 1/RTotal = 1/6 + 1/3 + 1/6
    # 1/RTotal = 2/3
    # RTotal = 3/2 = 1.5

### Examples

    parallel_resistance([6, 3]) ➞ 2
    
    parallel_resistance([10, 20, 10]) ➞ 4
    
    parallel_resistance([500, 500, 500]) ➞ 166.6
    # Round to the nearest decimal place

### Notes

  *  **Note that you should rearrange to return the RTotal, not 1 / RTotal.**
  * Round to the nearest decimal place.
  * All inputs will be valid.

"""

def parallel_resistance(lst):
  return round(1/sum([1/x for x in lst]),1)

