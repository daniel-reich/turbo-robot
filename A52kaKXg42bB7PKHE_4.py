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
    l = []
    for elem in lst:
        for e2 in elem:
            l.append(e2)
    l1 = sorted([x for x in l if type(x) == float or type(x) == int])
    l2 = sorted([x for x in l if type(x) == str])
    l3 = (l1+l2)[::-1]
    l_new = []
    
    for elem in lst:
        l_block = []
        for e2 in elem:
            l_block.append(l3.pop())
        l_new.append(l_block)
    return l_new

