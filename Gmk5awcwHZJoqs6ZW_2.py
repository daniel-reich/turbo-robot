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
    if len(lst)==1:return 1
    l=[(x,y) for x in range(len(lst)) for y in range(len(lst[x])) if lst[x][y]==1]
    t=0
    l2=[]
    for i in l:
        if (i[0] + 1, i[1] + 1) in l and (i[0] + 1, i[1] + 1) not in l2:
            l2.append((i[0] + 1, i[1] + 1))
            t+=1
        if (i[0] - 1, i[1] + 1) in l and  (i[0] - 1, i[1] + 1) not in l2:
            l2.append((i[0] - 1, i[1] + 1))
            t+=1
        if (i[0] - 1, i[1] - 1) in l and (i[0] - 1, i[1] - 1) not in l2:
            l2.append((i[0] - 1, i[1] - 1))
            t+=1
        if (i[0] + 1, i[1] - 1) in l and  (i[0] + 1, i[1] - 1) not in l2:
            l2.append((i[0] + 1, i[1] - 1))
            t+=1
        if (i[0] + 1, i[1]) in l and (i[0] + 1, i[1]) not in l2 :
            l2.append((i[0] + 1, i[1]))
            t+=1
        if (i[0] - 1, i[1]) in l and (i[0] - 1, i[1]) not in l2:
            l2.append((i[0] - 1, i[1]))
            t+=1
        if (i[0], i[1] - 1) in l and (i[0], i[1] - 1) not in l2 :
            l2.append((i[0], i[1] - 1) )
            t+=1
        if (i[0], i[1] + 1) in l and (i[0], i[1] + 1) not in l2:
            l2.append((i[0], i[1] + 1))
            t+=1
    if t==0:return 1        
    return t

