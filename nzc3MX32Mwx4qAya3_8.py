"""


Write a function that reverses the sublist between the start and end index (
**inclusive** ). The rest of the list should be kept the same.

### Examples

    ranged_reversal([1, 2, 3, 4, 5, 6], 1, 3) ➞ [1, 4, 3, 2, 5, 6]
    
    ranged_reversal([1, 2, 3, 4, 5, 6], 0, 4) ➞ [5, 4, 3, 2, 1, 6]
    
    ranged_reversal([9, 8, 7, 4], 0, 0) ➞ [9, 8, 7, 4]

### Notes

  * Lists will be zero-indexed.
  * The start and end indices will always be valid in context of the list.
  * The end index will always be greater than or equal to the starting index.
  * Return the list itself if the starting and ending index are the same.

"""

def ranged_reversal(lst, start, finish):
  subsection = lst[start:(finish+1)]
  revsubsection = subsection[::-1]
  newlist = lst[:start]+revsubsection+lst[(finish+1):]
  return newlist

