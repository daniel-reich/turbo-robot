"""


You will be given two **extremely** similar lists, but exactly one of the
items in a list will be valued slightly higher than its counterpart (which
means that evaluating **the value > the other value** will return `True`).

Create a function that returns whether the first list is _slightly superior_
to the second list.

### Worked Example

    is_first_superior([1, 2, 4], [1, 2, 3]) ➞ True
    # The pair of items at each index are compared in turn.
    # 1 from the first list is the same as 1 from the second list.
    # 2 is the same as 2.
    # However, 4 is greater than 3, so list one is superior.

### Examples

    is_first_superior(["a", "d", "c"], ["a", "b", "c"]) ➞ True
    
    is_first_superior(["zebra", "ostrich", "whale"], ["ant", "ostrich", "whale"]) ➞ True
    
    is_first_superior([1, 2, 3, 4], [1, 2, 4, 4]) ➞ False
    
    is_first_superior([True, 10, "zebra"], [True, 10, "zebra"]) ➞ False

### Notes

  * Both lists will be the same length.
  * All values and their counterparts will always be the same data type.
  * The lists will only be different by **one** element.
  * If the two lists are the same, return `False`.

"""

def is_first_superior(lst1, lst2):
  if lst1 > lst2:
    return True 
  else:
    return False

