"""


Write a function that returns `True` if two lists have the same number of
**unique** elements, and `False` otherwise.

To illustrate:

    lst1 = [1, 3, 4, 4, 4]
    lst2 = [2, 5, 7]

In `lst1`, the number `4` appears three times, which means it contains three
unique elements: `[1, 3, 4]`. Since `lst1` and `lst2` both contain the same
number of **unique** elements, this example would return `True`.

### Examples

    same([1, 3, 4, 4, 4], [2, 5, 7]) ➞ True
    
    same([9, 8, 7, 6], [4, 4, 3, 1]) ➞ False
    
    same([2], [3, 3, 3, 3, 3]) ➞ True

### Notes

N/A

"""

def same(a1, a2):
  uniqueA1 = []
  uniqueA2 = []
  
  for item in a1:
    if item not in uniqueA1:
      uniqueA1.append(item)
  for item in a2:
    if item not in uniqueA2:
      uniqueA2.append(item)
  return len(uniqueA1) == len(uniqueA2)

