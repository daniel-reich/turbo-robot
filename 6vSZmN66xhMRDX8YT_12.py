"""


Create a function that takes a list of **numbers or strings** and returns a
list with the items from the original list stored into sublists. Items of the
same value should be in the same sublist.

### Examples

    advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]
    
    advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]
    
    advanced_sort(["b", "a", "b", "a", "c"]) ➞ [["b", "b"], ["a", "a"], ["c"]]

### Notes

The sublists should be returned in the order of each element's first
appearance in the given list.

"""

def advanced_sort(lst):
    final_list=[]
    for val in lst:
        count=lst.count(val)
        new_list=[val for i in range(count)]
        if new_list not in final_list:
            final_list.append(new_list)
    return final_list

