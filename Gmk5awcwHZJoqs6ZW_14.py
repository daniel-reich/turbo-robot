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
    def find_starter(lst,checked):
            for y in range(ylen):
                for x in range(xlen):
                    if lst[y][x]==1 and (y,x) not in checked:
                        return (y,x)
            return False
        
    checked,ylen,xlen,to_check=[],len(lst),len(lst[0]),[]
    neigh=[(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]
    res=[]
    while find_starter(lst,checked):
        count=0
        to_check=[find_starter(lst,checked,)]
        while to_check:            
            for cell in to_check:
                to_check.remove(cell)
                y,x=cell[0],cell[1]
                count+=1
                checked.append((y,x))
                for n in neigh:
                    if y+n[0] in range(ylen) and x+n[1] in range(xlen) and lst[y+n[0]][x+n[1]] ==1 and (y+n[0],x+n[1]) not in checked:
                        if (y+n[0],x+n[1]) not in to_check:
                            to_check.append((y+n[0],x+n[1])) 
        res.append(count)    
    return max(res)

