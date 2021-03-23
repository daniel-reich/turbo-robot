"""


Given an int, figure out how many ones, threes and nines you could fit into
the number. You must create a class. You will make variables (`self.ones`,
`self.threes`, `self.nines`) to do this.

### Examples

    n1 = ones_threes_nines(5)
    n1.nines ➞ 0
    
    n1.ones ➞ 5
    
    n1.threes ➞ 1

### Notes

  * Do not use the math module.
  * See [version #2](https://edabit.com/challenge/8Fwv2f8My4kcNjMZh) of this series.

"""

class ones_threes_nines:
  def __init__ (self,n):
    self.threes = 0
    self.nines = 0
    self.ones = n
    if n % 3 == 0:
      self.threes = int(n/3)
    else:
      self.threes = int(n/3)
    if n % 9 == 0:
      self.nines = int(n/9)
    else:
      self.nines = int(n/9)

