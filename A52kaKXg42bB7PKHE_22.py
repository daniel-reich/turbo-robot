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
  lst_dict = {}
  num = []
  char = []
  for i in range(len(lst)):
    lst_dict[i] = len(lst[i])
    for j in range(len(lst[i])):
      if str(lst[i][j]).isalpha():
        char.append(lst[i][j])
      else:
        num.append(lst[i][j])
  lst = (sorted(num) + sorted(char))
  ans = []
  v = 0
  for j in lst_dict:
    ans.append(lst[v: lst_dict[j] + v])
    v += lst_dict[j]
  return ans

