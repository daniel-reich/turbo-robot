"""


Given an integer between 0 and 26, make a variable (self.answer). That
variable would be assigned to a string in this format:

    "nines:your answer, threes:your answer, ones:your answer"

You need to find out how many ones, threes, and nines it would at least take
for the number of each to add up to the given integer when multiplied by one,
three or nine (depends).

### Examples

    ones_threes_nines(10) ➞ "nines:1, threes:0, ones:1"
    
    ones_threes_nines(15) ➞ "nines:1, threes:2, ones:0"
    
    ones_threes_nines(22) ➞ "nines:2, threes:1, ones:1"

### Notes

  * Each of the ones, threes or nines could only be either 0, 1 or 2.
  * You must use a class.
  * After the comma, you must put a space.
  * See [version #1](https://edabit.com/challenge/X6xZ2EaqqQbGF7Bwv) of this series.

"""

class ones_threes_nines:
  def __init__(self,num):
    nines = num//9
    num -= nines*9
    threes = num//3
    num -= threes*3
    self.answer = "nines:"+str(nines)+", threes:"+str(threes)+", ones:"+str(num)

