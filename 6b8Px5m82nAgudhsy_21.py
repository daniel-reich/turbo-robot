"""


Write a function that returns the next number that can be created from the
same digits as the input.

### Examples

    next_number(19) ➞ 91
    
    next_number(3542) ➞ 4235
    
    next_number(5432) ➞ 5432
    
    next_number(58943) ➞ 59348

### Notes

  * If no larger number can be formed, return the number itself.
  *  **Bonus** : See if you can do this without generating all digit permutations.

"""

import itertools
​
​
def next_number(num):
    r = [x for x in str(num)]
    lol = list(set(sorted([int("".join(i)) for i in list(itertools.permutations(r))])))
    lol.sort()
    if lol.index(num) == len(lol)-1:
        return num
    else:
        return lol[lol.index(num)+1]

