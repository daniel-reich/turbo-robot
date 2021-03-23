"""


Create a function that takes a two-dimensional list as an argument and returns
a one-dimensional list with the values of the original 2d list that are
arranged by spiralling through it (starting from the top-left).

### Examples

    spiral_transposition([
      [7, 2],
      [5, 0]
    ])
    
    ➞ [7, 2, 0, 5]
    
    spiral_transposition([
      [1, 2, 3],  
      [4, 5, 6],
      [7, 8, 9]
    ])
    
    ➞ [1, 2, 3, 6, 9, 8, 7, 4, 5]
    
    spiral_transposition([
      [1, 1, 1],  
      [4, 5, 2],
      [3, 3, 2] 
    ])
    
    ➞ [1, 1, 1, 2, 2, 3, 3, 4, 5]

### Notes

If you do not understand the instructions, write the 3x3 list example on a
piece of paper and trace the output through it.

"""

def pop_up(lst):
  if not lst: return []
  return lst.pop(0)
​
def pop_right(lst):
  if not lst: return []
  return [row.pop() for row in lst]
​
def pop_down(lst):
  if not lst: return []
  return lst.pop()[::-1]
​
def pop_left(lst):
  if not lst: return []
  return [row.pop(0) for row in lst][::-1]
​
def append(lst, result):
  if lst:
    [result.append(x) for x in lst]
​
def spiral_transposition(lst):
  result = []
  while lst:
    append(pop_up(lst),result)
    append(pop_right(lst),result)
    append(pop_down(lst),result)
    append(pop_left(lst),result)
  return result

