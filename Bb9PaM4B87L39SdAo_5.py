"""


Create a function takes in two lists and returns an **intersection list** and
a **union list**.

  1.  **Intersection List:** Elements shared by both.
  2.  **Union List:** Elements that exist in first or second list, or both (not exclusive OR).

While the input lists may have duplicate numbers, the returned
**intersection** and **union** lists should be _set-ified_ \- that is, contain
no duplicates. Returned lists should be sorted in **ascending** order.

    List 1: [5, 6, 6, 6, 8, 9]
    List 2: [3, 3, 4, 4, 5, 5, 8]
    
    Intersection: [5, 8]
    # 5 and 8 are the only 2 numbers that exist in both lists.
    
    Union: [3, 4, 5, 6, 8, 9]
    # Each number exists in at least one list.

### Examples

    intersection_union([1, 2, 3, 4, 4], [4, 5, 9]) ➞ [[4], [1, 2, 3, 4, 5, 9]]
    
    intersection_union([1, 2, 3], [4, 5, 6]) ➞ [[], [1, 2, 3, 4, 5, 6]]
    
    intersection_union([1, 1], [1, 1, 1, 1]) ➞ [[1], [1]]

### Notes

  * Order of output should be: `[Intersection], [Union]`.
  * Remember both output lists should be in **ascending order**.
  * Each input list will have at least one element.
  * If both lists are disjoint (share nothing in common), return an empty list `[]` for the intersection.

"""

def intersection_union(lst1, lst2):
    int_sec = set(lst1).intersection(set(lst2))
    union_list = set(lst1).union(set(lst2))
    return [sorted(int_sec), sorted(union_list)]

