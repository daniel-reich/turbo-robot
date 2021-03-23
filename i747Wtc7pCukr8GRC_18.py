"""


Write **two** functions:

  1. One that returns the **maximum product** of three numbers in a list.
  2. One that returns the **minimum product** of three numbers in a list.

### Examples

    max_product([-8, -9, 1, 2, 7]) ➞ 504
    
    max_product([-8, 1, 2, 7, 9]) ➞ 126
    
    min_product([1, -1, 1, 1]) ➞ -1
    
    min_product([-5, -3, -1, 0, 4]) ➞ -15

### Notes

N/A

"""

def max_product(lst):
    max_num = lst[0] * lst[1] * lst[2]
    for i in range(len(lst)):
        for x in range(len(lst)):
            for z in range(len(lst)):
                if max_num < lst[i] * lst[x] * lst[z] and not i == x and not i == z and not x == z:
                    max_num = lst[i] * lst[x] * lst[z]
    return max_num
​
​
​
​
def min_product(lst):
    max_num = lst[0] * lst[1] * lst[2]
    for i in range(len(lst)):
        for x in range(len(lst)):
            for z in range(len(lst)):
                if max_num > lst[i] * lst[x] * lst[z] and not i == x and not i == z and not x == z:
                    max_num = lst[i] * lst[x] * lst[z]
    return max_num

