"""


An **island is a region of contiguous ones**. A contiguous one is a `1` that
is touched by at least one other `1`, either **horizontally** , **vertically**
or **diagonally**. Given a piece of the map, represented by a 2-D list, create
a function that returns the area of the largest island.

To illustrate, if we were given the following piece of the map, we should
return `4`.

    [
      [0, 0, 0],
      [0, 1, 1],
      [0, 1, 1]
    ]

Our function should yield `2` for the map below:

    [
      [1, 0, 0],
      [0, 0, 1],
      [0, 0, 1]
    ]

Our function should yield `4` for the map below: :

    [
      [1, 0, 0],
      [0, 1, 1],
      [0, 0, 1]
    ]

### Examples

    largest_island([
      [1, 0, 0], 
      [0, 0, 0], 
      [0, 0, 1]
    ])
    
    ➞ 1
    
    largest_island([
      [1, 1, 0], 
      [0, 1, 1], 
      [0, 0, 1]
    ])
    
    ➞ 5
    
    largest_island([
      [1, 0, 0], 
      [1, 0, 0], 
      [1, 0, 1]
    ])
    
    ➞ 3

### Notes

  * Maps can be any `m x n` dimension.
  * Maps will always have at least 1 element. `m >= 1` and `n >= 1`.

"""

def largest_island(lst):
  mx=0
  for i in range(len(lst)):
    for x in range(len(lst[i])):
      marked=[]
      if lst[i][x]==1:
        marked.append([i,x])
        marked = findisland(marked,lst)
        if len(marked)>mx:
          mx = len(marked)
  return mx
​
def findisland(marked,lst):
  init = marked
  for i in init:
    marked = leftright(lst,i,marked)
    marked = updown(lst,i,marked)
    marked = diag(lst,i,marked)
  if len(init)<len(marked):
    marked = findisland(marked,lst)
  else:
    return marked
​
def leftright(lst, place, marked):
  if place[1] > 0:
    if lst[place[0]][place[1]-1] == 1 and [place[0],place[1]-1] not in marked:
      marked.append([place[0],place[1]-1])
  if place[1] < len(lst[0])-1:
    if lst[place[0]][place[1]+1] and [place[0],place[1]+1] not in marked:
      marked.append([place[0],place[1]+1])
  return marked
  
def updown(lst, place, marked):
  if place[0] > 0:
    if lst[place[0]-1][place[1]] == 1 and [place[0]-1,place[1]] not in marked:
      marked.append([place[0]-1,place[1]])
  if place[0] < len(lst)-1:
    if lst[place[0]+1][place[1]] and [place[0]+1,place[1]] not in marked:
      marked.append([place[0]+1,place[1]])
  return marked
  
def diag(lst, place, marked):
  if place[0] > 0 and place[1] > 0:
    if lst[place[0]-1][place[1]-1] == 1 and [place[0]-1,place[1]-1] not in marked:
      marked.append([place[0]-1,place[1]-1])
  if place[0] < len(lst)-1 and place[1] < len(lst[0])-1:
    if lst[place[0]+1][place[1]+1] and [place[0]+1,place[1]+1] not in marked:
      marked.append([place[0]+1,place[1]+1])
  if place[0] > 0 and place[1] < len(lst[0])-1:
    if lst[place[0]-1][place[1]+1] == 1 and [place[0]-1,place[1]+1] not in marked:
      marked.append([place[0]-1,place[1]+1])
  if place[0] < len(lst)-1 and place[1] > 0:
    if lst[place[0]+1][place[1]-1] and [place[0]+1,place[1]-1] not in marked:
      marked.append([place[0]+1,place[1]-1])
  return marked

