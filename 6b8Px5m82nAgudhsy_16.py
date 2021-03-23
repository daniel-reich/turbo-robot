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

def permute(k, n, lst, state, str_number):
    if k == 0:
        new_number = " "
        for i in range(n):
            new_number += str_number[state[i]]
        if int(new_number) > int(str_number):
            lst.append(int(new_number))
    for i in range(n):
        if i not in state:
            state.append(i)
            permute(k-1, n, lst, state, str_number)
            state.pop()
​
​
def next_number(number):
    str_number = str(number)
    n = len(str_number)
    lst = []
    permute(n, n, lst, [], str_number)
    lst.sort()
    if lst:
        return lst[0]
    else:
        return number

