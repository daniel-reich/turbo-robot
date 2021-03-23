"""


Create a function that takes a string and returns the right answer.

### Examples

    post_fix("2 2 +") ➞ 4
    
    post_fix("2 2 /") ➞ 1
    
    post_fix("8 4 / 9 * 3 1 * /") ➞ 54

### Notes

  * The operators `+ - * /` may be supported.
  * Output always returns an integer.

"""

from itertools import permutations
def post_fix(expr):
    for p in permutations(expr.split(" ")):
        try:
            if eval(" ".join(p)) == int(eval(" ".join(p))):
                return int(eval(" ".join(p)))
        except:
            pass

