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
  x=[a1[i]+a2[i] for i in range(min(len(a1),len(a2)))]
  return all([x[i]==x[i-1] for i in range(1,min(len(a1),len(a2)))]) and len(a1)==len(a2)

