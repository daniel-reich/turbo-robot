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
  def __init__(a,n):a.ones,a.threes,a.nines=n,n//3,n//9

