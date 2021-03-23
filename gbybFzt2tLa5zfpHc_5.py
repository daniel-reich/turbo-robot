"""


Write a function that returns all sets of three elements that sum to 0.

### Examples

    three_sum([0, 1, -1, -1, 2]) ➞ [[0, 1, -1], [-1, -1, 2]]
    
    three_sum([0, 0, 0, 5, -5]) ➞ [[0, 0, 0], [0, 5, -5]]
    
    three_sum([1, 2, 3]) ➞ []
    
    three_sum([1]) ➞ []

### Notes

  * The original list **may contain duplicate numbers**.
  * Each three-element sublist in your output should be **distinct**.
  * Sublists should be ordered by the first element of the sublist.
  * Sublists themselves should be ordered the same as the original list.
  * Return an empty list if no three elements sum to zero.
  * Return an empty list if there are fewer than three elements.

"""

def three_sum(lst):
  import itertools
  output = []
  for n in itertools.combinations(lst, 3):
    n = list(n)
    if n[0]+n[1]+n[2]==0 and n not in output:
      output.append(n)
  return output

