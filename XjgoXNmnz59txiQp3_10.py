"""


About a month ago I stumbled upon an interesting problem — something called
the 25 split. In the problem, you had to break up 25 into parts that add to
it, and, from those parts, try to create the biggest product.

For example, `3 * 22 = 66` or `5 * 5 * 5 * 5 * 5 = 3125`. With this first
part, return the value of the biggest product possible using natural number
parts from a given number, _x_.

### Examples

    split(5) ➞ 6
    # 3 times 2
    
    split(10) ➞ 36
    # 3 * 3 * 4
    
    split(1) ➞ 1

### Notes

  * 3's are useful...
  * Part 2 of this challenge is [here](https://edabit.com/challenge/jyHs9YRnrPgLwKiaL).

"""

from itertools import combinations_with_replacement
import numpy as np
def split(number):
  lst, candidates = [i+1 for i in range(number)],[number]
  rr= 1 if number<=10 else 2.5 if (number >10 and number<=20) else 2.7
  for j in range (1,int((number+1)/rr)):
    for i in (list (combinations_with_replacement(lst,j))):
      if sum(i)==number:
        candidates.append(np.prod(np.array(i)))
  return (max(candidates))

