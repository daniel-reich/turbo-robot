"""


Create a function that takes an expression `exp` and an upper limit `i` as
arguments and returns the sum of that expression up to the i'th term (recall
sigma from math class).

### Examples

    summation("n", 10) ➞ 55
    
    summation("1/n", 50) ➞ 4.5
    
    summation("n**n", 6) ➞ 50069

### Notes

  * Assume the lower limit is `i = 1`.
  * Round your answer to the nearest tenth.

"""

def summation(exp, num):
  to_add = []
  for n in range(1, num + 1):
    to_add.append(eval(exp))
  return round(sum(to_add),1)

