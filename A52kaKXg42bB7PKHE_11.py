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
    v = []
    w = []
    g = []
    s = []
    for i in lst:
        for y in i:
            v.append(y)
    for i in v:
        if i is str(i):
            w.append(i)
        else:
            g.append(i)
    g.sort()
    w.sort()
    r = g + w
    row = len(lst)
    cols = list(map(len, lst))
    p = 0
    k = cols[0]
    for i in range(1, row):
        s.append(r[p:k])
        p = k
        k += cols[i]
​
    s.append(r[p:k])
    return s

