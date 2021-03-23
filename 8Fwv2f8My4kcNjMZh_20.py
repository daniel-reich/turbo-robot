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
    def __init__(self, num):
        self.num = num
        self.answer = None
        if self.num <= 26:
            if self.num / 9 > 0:
                by_9 = int(self.num/9)
                if (self.num - 9*by_9)/3 > 0:
                    by_3 = int((self.num - 9*by_9)/3)
                    by_1 = (self.num - 3*by_3 - 9*by_9)
            self.answer = "nines:" + \
                str(by_9) + ", threes:" + str(by_3) + ", ones:" + str(by_1)

