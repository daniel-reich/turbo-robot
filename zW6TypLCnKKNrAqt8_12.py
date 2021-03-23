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
  ans = [0]
  for i in range(0, len(lst) - 1):
    s = list(filter(lambda x: x < lst[i+1], lst[0:i+1]))
    ans.append(len(s))
  return ans
​
def right_side(lst):
  ans = []
  for i in range(0, len(lst) - 1):
    s = list(filter(lambda x: x < lst[i], lst[i+1:]))
    ans.append(len(s))
  ans.append(0)
  return ans

