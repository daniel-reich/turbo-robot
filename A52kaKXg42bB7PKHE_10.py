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
    num_list, str_list, len_list = [], [], []
    for slist in lst:
        len_list.append(len(slist))
        for item in slist:
            if type(item) is int or type(item) is float:
                num_list.append(item)
            else:
                str_list.append(item)
    num_list.sort()
    str_list.sort()
    num_list.extend(str_list)
    return_list = []
    for i in range(len(len_list)):
        temp_list = [item for n, item in enumerate(num_list) if n < len_list[i]]
        return_list.append(temp_list)
        del num_list[0:len_list[i]]
    return return_list

