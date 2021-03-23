"""


Create a function that takes a number `a` and finds the missing exponent _x_
so that `a` when raised to the power of _x_ is equal to `b`.

### Examples

    solve_for_exp(4, 1024) ➞ 5
    
    solve_for_exp(2, 1024) ➞ 10
    
    solve_for_exp(9, 3486784401) ➞ 10

### Notes

`a` is raised to the power of what in order to equal `b`?

"""

def solve_for_exp(a, b):
  power = 0
  while True:
    if pow(a,power) == b:
      return power
    power += 1

