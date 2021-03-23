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
  slst = []
  for i in lst:
    for j in i:
      slst.append(j)
  flst, j, slst = [], 0, sorted([a for a in slst if type(a) != str]) + sorted([b for b in slst if type(b) == str])
  while j != len(lst):
    i, f = 0, []
    while i != len(lst[j]): f.append(slst[i + sum(len(lst[x]) for x in range(j)) if j else i]); i += 1
    flst.append(f); j += 1
  return flst

