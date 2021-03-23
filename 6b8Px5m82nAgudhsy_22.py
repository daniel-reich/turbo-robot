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

from itertools import permutations
​
​
def next_number(num):
    try:
        perms = list(permutations(str(num)))
        j = ["".join(i) for i in perms]
        inted = [int(i) for i in j]
        return sorted([i for i in inted if i > num])[0]
    except IndexError:
        return num

