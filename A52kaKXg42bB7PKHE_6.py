"""


Write a function that sorts list while keeping the list structure. Numbers
should be first then letters both in ascending order.

### Examples

    num_then_char([
      [1, 2, 4, 3, "a", "b"],
      [6, "c", 5], [7, "d"],
      ["f", "e", 8]
    ]) ➞ [
      [1, 2, 3, 4, 5, 6],
      [7, 8, "a"],
      ["b", "c"], ["d", "e", "f"]
    ]
    
    num_then_char([
      [1, 2, 4.4, "f", "a", "b"],
      [0], [0.5, "d","X",3,"s"],
      ["f", "e", 8],
      ["p","Y","Z"],
      [12,18]
    ]) ➞ [
      [0, 0.5, 1, 2, 3, 4.4],
      [8],
      [12, 18, "X", "Y", "Z"],
      ["a", "b", "d"],
      ["e", "f", "f"],
      ["p", "s"]
    ]

### Notes

Test cases will contain integer and float numbers and single letters.

"""

from itertools import chain
def num_then_char(lst):
  len_list = [len(i) for i in lst]
  unp_list = list(chain.from_iterable(lst))
  sorted_list = sorted(i for i in unp_list if type(i) in (int, float)) \
          + sorted(i for i in unp_list if type(i) == str)
  result = []
  for i in len_list:
    add_list = []
    for _ in range(i):
      add_list.append(sorted_list.pop(0))
    result.append(add_list)
  return result

