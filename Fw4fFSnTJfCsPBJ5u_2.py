"""


Create a function which calculates how many numbers are missing from an
**ordered** number line. This number line starts at the first value of the
list, and increases by 1 to the end of the number line, ending at the last
value of the list.

    how_many_missing([1, 2, 3, 8, 9]) ➞ 4
    
    # The number line starts at 1 and ends at 9 (so the numbers 0 and 10 aren't missing from it).
    # The numbers missing from this line are 4, 5, 6, and 7.
    # 4 numbers are missing.

### Examples

    how_many_missing([1, 3]) ➞ 1
    
    how_many_missing([7, 10, 11, 12]) ➞ 2
    
    how_many_missing([1, 3, 5, 7, 9, 11]) ➞ 5
    
    how_many_missing([5, 6, 7, 8]) ➞ 0

### Notes

If the number line is complete, or the list is empty, return `0`.

"""

def how_many_missing(lst):
  if len(lst) <2:
    return 0
  return (lst[-1]-lst[0]+1)-len(lst)

