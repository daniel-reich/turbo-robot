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

def num_then_char(lst):
  inner_sizes = [len(inner) for inner in lst]
  new_lst = [i for inner in lst for i in inner]
  num_lst = sorted([i for i in new_lst if (type(i) == type(1) or type(i)==type(1.1))])
  char_lst = sorted([i for i in new_lst if type(i) == type('a')])
  lst = num_lst + char_lst
  ans = []
  for size in inner_sizes:
    temp = []
    for i in range(size):
      temp.append(lst.pop(0))
    ans.append(temp)
  return ans

