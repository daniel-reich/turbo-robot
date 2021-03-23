"""


Create a function that takes a list of numbers `lst`, a string `s` and return
a list of numbers as per the following rules:

  * `"Asc"` returns a sorted list in ascending order.
  * `"Des"` returns a sorted list in descending order.
  * `"None"` returns a list without any modification.

### Examples

    asc_des_none([4, 3, 2, 1], "Asc" ) ➞ [1, 2, 3, 4]
    
    asc_des_none([7, 8, 11, 66], "Des") ➞ [66, 11, 8, 7]
    
    asc_des_none([1, 2, 3, 4], "None") ➞ [1, 2, 3, 4]

### Notes

N/A

"""

def asc_des_none(lst, s):
  print(lst,s)
  new_list = []
  if s == 'None':
    return lst
  elif s == 'Asc':
    while lst:
      x = lst[0]
      for i in lst:
        if i < x:
          x = i
      new_list.append(x)
      lst.remove(x)
  elif s == 'Des':
    while lst:
      x = lst[0]
      for i in lst:
        if i > x:
          x = i
      new_list.append(x)
      lst.remove(x)
  print(lst)
  print(new_list)
  return new_list

