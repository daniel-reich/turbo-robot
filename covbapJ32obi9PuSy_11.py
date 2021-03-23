"""


Create a function that returns an array that expands by 1 from 1 to the value
of the input, and then reduces back to 1. Items in the lists will be the same
as the length of the lists.

### Examples

    diamond_arrays(1) ➞ [[1]]
    
    diamond_arrays(2) ➞ [[1], [2, 2], [1]]
    
    diamond_arrays(5) ➞ [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5], [4, 4, 4, 4], [3, 3, 3], [2, 2], [1]]

### Notes

N/A

"""

def diamond_arrays(x):
  def create_half(size):
    if size == 1:
      return [1]
    elif size < 1:
      return []
    else:
      return [size] * size + create_half(size - 1)
  def nest(lst):
    nests = []
    prev = 0
    nest = []
    
    for n in range(len(lst)):
      item = lst[n]
      if item != prev:
        if nest != []:
          nests.append(nest)
        nest = [item]
        prev = item
      else:
        nest.append(item)
    
    if nest != []:
      nests.append(nest)
    
    return nests
        
  
  front_half = list(reversed(create_half(x-1)))
  back_half = create_half(x)
  
  return nest(front_half + back_half)

