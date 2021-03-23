"""


Write a function that divides a list into chunks such that the sum of each
chunk is `<= n`. Start from the left side of the list and move to the right.

### Examples

    divide([1, 2, 3, 4, 1, 0, 2, 2], 5)
    ➞ [[1, 2], [3], [4, 1, 0], [2, 2]]
    
    divide([1, 0, 1, 1, -1, 0, 0], 1)
    ➞ [[1, 0], [1], [1, -1, 0, 0]]
    
    divide([2, 1, 0, -1, 0, 0, 2, 1, 3], 3)
    ➞ [[2, 1, 0, -1, 0, 0], [2, 1], [3]]

### Notes

  * The max of the list will always be smaller than or equal to `n`.
  * Use the **greedy approach** when solving the problem (e.g. fit as many elements you can into a chunk as long as you satisfy the sum constraint).

"""

def divide(lst, n):
  def divide(lst, n):
    chunk = []
    index = 0
​
    while sum(chunk) <= n and index < len(lst):
      chunk.append(lst[index])
      index += 1
      
    if sum(chunk) > n:
      chunk.pop(-1)
    
    if chunk == lst:
      return chunk, []
    
    for n in range(len(chunk)):
      lst.pop(0)
    
    return chunk, lst
  
  chunks = []
  c = 0
​
  while len(lst) > 0 and c < 1000:
    d = divide(lst, n)
    chunks.append(d[0])
    lst = d[1]
​
  return chunks

