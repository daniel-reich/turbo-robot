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
​
    unpck_lst = [ea for each in lst for ea in each]
    full_lst = sorted([x for x in unpck_lst if type(x) == int or type(x) == float])\
                + sorted([x for x in unpck_lst if type(x) == str])
    temp = 0
    final = []
    for each in lst:
        final.append(full_lst[temp:len(each)+temp])
        temp += len(each)
        
    return final

