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

from itertools import permutations as perm
​
​
def next_number(num):
    nums = sorted(set(int(''.join(i)) for i in perm(str(num)))) 
    main_num = nums.index(num)
    return num if nums[main_num] == nums[-1] else nums[main_num + 1]

