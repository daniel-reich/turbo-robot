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
    alp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cnt = [len(i) for i in lst]
    num = sorted([str(j) for i in lst for j in i if type(j) == int or type(j) == float], key = float)
    let = sorted([j for i in lst for j in i if type(j) == str])
    idx = 0; res = []; aux = []
    for i in num+let:
        if len(aux) < cnt[idx]: aux.append(float(i) if '.' in i else i if i in alp else int(i))
        else: res.append(aux); aux = []; aux.append(float(i) if '.' in i else i if i in alp else int(i)); idx += 1
    res.append(aux)
    return res

