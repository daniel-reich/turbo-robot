"""


Write a function that pairs the first number in an array with the last, the
second number with the second to last, etc.

### Examples

    pairs([1, 2, 3, 4, 5, 6, 7]) ➞ [[1, 7], [2, 6], [3, 5], [4, 4]]
    
    pairs([1, 2, 3, 4, 5, 6]) ➞ [[1, 6], [2, 5], [3, 4]]
    
    pairs([5, 9, 8, 1, 2]) ➞ [[5, 2], [9, 1], [8, 8]]
    
    pairs([]) ➞ []

### Notes

  * If the list has an **odd length** , repeat the middle element twice for the last pair.
  * Return an empty list if the input is an empty list.

"""

def pairs(lst):
  result, i = [], 0
  while len(result) < len(lst) / 2:
    result.append([lst[i], lst[-(1 + i)]])
    i += 1
  return result
