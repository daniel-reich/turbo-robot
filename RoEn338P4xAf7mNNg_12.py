"""


Given a rectangular grid of m by n spaces, signaled by 0s, and a number of
points, signaled by 1, 2, 3..., return the number of moves for the shortest
path that starts at 1 and goes over all the other points in ascending order.

### Examples

    shortest_path([
      ("001"),
      ("002"),
      ("003")
    ]) ➞ 2
    
    shortest_path([
      ("00000"),
      ("01006"),
      ("02000"),
      ("30050"),
      ("00004")
    ]) ➞ 13
    
    shortest_path([
      ("00020000"),
      ("01000000")
    ]) ➞ 3

### Notes

  * Only horizontal and vertical movements are allowed.
  * All movements from one place to an adjacent one count as 1 regardless of direction.
  * The points range from 1 to at most 9 with no repeating or missing digits.

"""

def shortest_path(lst):
​
    vert_indeces, point = [],1
    while str(point) in [i for j in lst for i in j]:
        for ind,j in enumerate(lst):
            if str(point) in j: vert_indeces.append(ind)
        point+=1
    
    vert_sum=0
    for ind,i in enumerate(vert_indeces):
        try: vert_sum+=abs(vert_indeces[ind]-vert_indeces[ind+1])
        except IndexError: break
​
    hor_indeces, point = [], 1
    while str(point) in [i for j in lst for i in j]:
        for i in vert_indeces:
            hor_indeces.append(lst[i].index(str(point)))
            point+=1
​
    hor_sum=0
    for ind,i in enumerate(hor_indeces):
        try: hor_sum+=abs(hor_indeces[ind]-hor_indeces[ind+1])
        except IndexError: break
    
    return vert_sum+hor_sum

