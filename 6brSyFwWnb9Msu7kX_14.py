"""


Write a function that sorts the **positive numbers** in **ascending order** ,
and keeps the **negative numbers** untouched.

### Examples

    pos_neg_sort([6, 3, -2, 5, -8, 2, -2]) ➞ [2, 3, -2, 5, -8, 6, -2]
    
    pos_neg_sort([6, 5, 4, -1, 3, 2, -1, 1]) ➞ [1, 2, 3, -1, 4, 5, -1, 6]
    
    pos_neg_sort([-5, -5, -5, -5, 7, -5]) ➞ [-5, -5, -5, -5, 7, -5]
    
    pos_neg_sort([]) ➞ []

### Notes

  * If given an empty list, you should return an empty list.
  * Integers will always be either positive or negative (0 isn't included in the tests).

"""

def pos_neg_sort(lst):
​
    negNumbers = []
    negNumbersIndex = []
    i = 0
​
    while i < len(lst):
        if lst[i] < 0:
            negNumbers.append(lst[i])
            negNumbersIndex.append(i)
        i += 1
    
    posArray = [y for y in lst if y > 0]
    posArray.sort()
​
    i2 = 0
    for negNumber in negNumbers:
        posArray.insert(negNumbersIndex[i2], negNumbers[i2])
        i2 += 1
    return(posArray)

