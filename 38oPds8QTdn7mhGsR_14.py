"""


The challange is simple. Return a random integer **N** such that `a` <= **N**
<= `b`.

### Examples

    random_int(5, 9) ➞ 7
    
    random_int(5, 9) ➞ 9
    
    random_int(5, 9) ➞ 5

### Notes

  * Don't forget to `return` the result.
  * Return value must be an integer.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.

"""

def random_int(a, b):
  import random
  return random.randint(a, b)

