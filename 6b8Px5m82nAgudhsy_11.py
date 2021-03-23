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
def next_number(num):
    lst=[]
    num1=list(map(str,str(num)))
    if len(num1)==1:
        return num
    elif num1[::-1]==sorted(num1):
        return num
    else:
        for i in list(permutations(num1)):
            lst.append(int("".join(i)))
        lst=list(set(lst))
        lst=sorted(lst)
    a=lst.index(num)
    return lst[a+1]

