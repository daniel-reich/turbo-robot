"""


Write a function that takes two lists and adds the first element in the first
list with the first element in the second list, the second element in the
first list with the second element in the second list, etc, etc. Return `True`
if all element combinations add up to the same number. Otherwise, return
`False`.

### Examples

    puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]) ➞ True
    # 1 + 4 = 5;  2 + 3 = 5;  3 + 2 = 5;  4 + 1 = 5
    # Both lists sum to [5, 5, 5, 5]
    
    puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]) ➞ True
    
    puzzle_pieces([1, 2], [-1, -1]) ➞ False
    
    puzzle_pieces([9, 8, 7], [7, 8, 9, 10]) ➞ False

### Notes

  * Each list will have at least one element.
  * Return `False` if both lists are of different length.

"""

def puzzle_pieces(a1, a2):
  if len(a1) == len(a2):
    a3 = [a1[x] + a2[x] for x in range(len(a2))]
    check = a1[0] + a2[0]
    if a3.count(check) == len(a1):
      return True
    else:
      return False
  else:
    return False

