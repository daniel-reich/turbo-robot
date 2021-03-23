"""


Write a function that moves all elements of one type to the **end** of the
list.

### Examples

    move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
    # Move all the 1s to the end of the array.
    
    move_to_end([7, 8, 9, 1, 2, 3, 4], 9) ➞ [7, 8, 1, 2, 3, 4, 9]
    
    move_to_end(["a", "a", "a", "b"], "a") ➞ ["b", "a", "a", "a"]

### Notes

Keep the order of the un-moved items the same.

"""

def move_to_end(lst, el):
  remove_count = 0
  for index in range(len(lst)-1,-1,-1):
    if(lst[index] == el):
      remove_count += 1
      lst.pop(index)
    
  while(remove_count > 0):
    lst.append(el)
    remove_count -= 1
    
  return lst

