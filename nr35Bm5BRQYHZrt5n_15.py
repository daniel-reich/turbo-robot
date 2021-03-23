"""


Create a function that determines if there is an upward trend.

### Examples

    upward_trend([1, 2, 3, 4]) ➞ True
    
    upward_trend([1, 2, 6, 5, 7, 8]) ➞ False
    
    upward_trend([1, 2, 3, "4"]) ➞ "Strings not permitted!"
    
    upward_trend([1, 2, 3, 6, 7]) ➞ True

### Notes

  * If there is a string element in the list, return `"Strings not permitted!"`.
  * The numbers don't have to be consecutive (e.g. `[1, 3, 5]` should still return `True`).

"""

def upward_trend(lst):
    for index in range (len(lst) -1):
        if isinstance(lst[index], str) or isinstance(lst[index + 1], str): return "Strings not permitted!"
        if lst[index] > lst[index + 1] :
            return False
    return True

