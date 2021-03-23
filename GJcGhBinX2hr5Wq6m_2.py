"""


Create a function that takes a list `lst` of numbers and **moves all zeros to
the end** , preserving the order of the other elements.

### Examples

    move_zeros([1, 0, 1, 2, 0, 1, 3]) ➞ [1, 1, 2, 1, 3, 0, 0]
    
    move_zeros([0, 1, None, 2, false, 1, 0]) ➞ [1, None, 2, false, 1, 0, 0]
    
    move_zeros(['a', 0, 0, 'b', 'c', 'd', 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) ➞ ['a', 'b', 'c', 'd', 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

### Notes

N/A

"""

def move_zeros(lst):
  zero_lst = []
  nonzero_lst =[]
  zero_lst.append([x for x in lst if (x == 0 and x is not False)])  
  nonzero_lst.append([x for x in lst if (x != 0 or x is False)])
  lst_sorted = nonzero_lst + zero_lst
  lst_final = [x for l in lst_sorted for x in l] #unpacking the list
​
  print(lst_final)
  return lst_final

