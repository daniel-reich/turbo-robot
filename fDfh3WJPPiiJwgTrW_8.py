"""


Return the total number of lists inside a given list.

### Examples

    num_of_sublists([[1, 2, 3]]) ➞ 1
    
    num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]) ➞ 3
    
    num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]) ➞ 4
    
    num_of_sublists([1, 2, 3]) ➞ 0

### Notes

N/A

"""

def num_of_sublists(lst):
  list_string = str(lst)
  list_string2 = list_string[1:len(list_string) - 1]
  count = 0
  for i in range(0, len(list_string2)):
    if list_string2[i] == "[":
      count+=1
  return count

