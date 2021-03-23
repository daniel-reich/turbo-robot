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
def next_number(num):
    if len(str(num))==1:return num
    l=[ x for x in str(num)]
    l2=[]
    for i in itertools.permutations(l,len(l)):
        if int("".join(list(i)))>num:l2.append(int("".join(list(i))))
    l2.sort()
    if len(l2)==0:return num
    return l2[0]

