"""


Write a function that returns `True` if all subsets in a list belong to a
given set.

### Examples

    validate_subsets([[1, 2], [2, 3], [1, 3]], [1, 2, 3]) ➞ True
    
    validate_subsets([[1, 2, 3], [2], [3], []], [1, 2, 3]) ➞ True
    
    validate_subsets([[1, 2], [2, 3], [1, 4]], [1, 2, 3]) ➞ False
    
    validate_subsets([[1, 2, 3, 4]], [1, 2, 3]) ➞ False

### Notes

  * The **empty set** and the **set** itself are **both** valid subsets of a set (we are not talking about proper subsets here).
  * The set and the subset will each have unique elements.

"""

def validate_subsets(subsets, my_set):
  subs = [set(sub) for sub in subsets]
  my_set = set(my_set)
  return all(False for sub in subs if not sub.issubset(my_set) )

