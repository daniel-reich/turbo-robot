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
  all_st=[item for list_item in lst for item in list_item if type(item) == str]
  all_num=[item for list_item in lst for item in list_item if not type(item) == str]
  all_st.sort()
  all_num.sort()
  
  counter=0
  for index,litem in enumerate(lst):
    for index_ll,ll in enumerate(litem):
      if counter<len(all_num):
        lst[index][index_ll]=all_num[counter]
      else:
        lst[index][index_ll]=all_st[counter - len(all_num)]
      counter+=1
  return(lst)

