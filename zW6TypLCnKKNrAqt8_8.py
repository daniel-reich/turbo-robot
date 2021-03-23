"""
Create two functions:

  1.  **Leftside function** : Returns count of numbers _strictly smaller_ than `n` on the left.
  2.  **Rightside function** : Returns count of numbers _strictly smaller_ than `n` on the right.

### Examples

    left_side([5, 2, 1, 4, 8, 7]) ➞ [0, 0, 0, 2, 4, 4]
    
    right_side([5, 2, 1, 4, 8, 7]) ➞ [3, 1, 0, 0, 1, 0]
    
    left_side([1, 2, 3, -1]) ➞ [0, 1, 2, 0]
    
    right_side([1, 2, 3, -1]) ➞ [1, 1, 1, 0]

### Notes

"Left" and "right" refer to the number at indices less than or greater than
`n`'s index, respectively.

"""

def left_side(lst):
  res = [0]
  for x in range(1,len(lst)):
    count =0
    for y in range(x):    
      if lst[x]> lst[y]:
        count+=1
    res.append(count)
  return res
  
def right_side(lst):
  res = []
  for x in range(len(lst)):
    count=0
    for y in range(x, len(lst)):
      if lst[x]> lst[y]:
        count+=1
    res.append(count)
  return res

