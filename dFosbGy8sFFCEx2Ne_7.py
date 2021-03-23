"""


R, a programming language used for Statistics and Data Analysis, has the
function `rank`, which returns the rank for each value in a vector.

For example:

    my_list = [1, 3, 3, 9, 8]
    # Ranked would be: [0, 1.5, 1.5, 4, 3]

When two or more values have the same rank, they are assigned the mean of
their rankings. Here, the two `3`s have ranks `1` and `2`, so both are
assigned rank `1.5`.

Implement the function `rank()` so that it works the same it does in R.

### Examples

    rank([9, 1, 4, 5, 4]) ➞ [4.0, 0.0, 1.5, 3.0, 1.5]
    
    rank(["z", "c", "f", "b", "c"]) ➞ [4.0, 1.5, 3.0, 0.0, 1.5]

### Notes

  * Expect numbers and lower-case alphabetic characters only.
  * Find Part I: Order [here](https://edabit.com/challenge/kQayLoFNx4QgWahHu).
  * Vectors in R are similar to a list. Although vectors in R are 1-indexed, your function should be 0-indexed. Other differences between vectors and lists will be ignored for the scope of this challenge.

"""

from bisect import *
​
def rank(lst):
  meh = sorted(lst)
  return [(bisect_left(meh,e)+bisect_right(meh,e)-1)/2 for e in lst]

