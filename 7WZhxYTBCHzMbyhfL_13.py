"""


You will be given the location of a knight, and an end location. The knight
can move in a "L" shape. "L" shape movement means that the knight can change
it's `x` coordinate by 2 and it's `y` coordinate by 1 or it can change it's
`y` coordinate by 2 and it's `x` coordinate by 1 (you can add and subtract
from the x/y).

For example, if the knight is at the position (0, 0), it can move to:

    (1,2), (1,-2), (2,1), (2,-1), (-1,2), (-1,-2), (-2,1), (-2, -1)

Your job is to return the least amount of steps needed to go from the position
K (knight's start position) to E (end). You will only be given the knight
starter coordinates (x1, y1) and the end coordinates (x2, y2).

Constrains: `1 <= x1,y1,x2,y2 <= 8`

### Examples

    knight_bfs(1, 1, 8, 8) ➞ 6
    
    knight_bfs(1, 1, 3, 2) ➞ 1
    
    knight_bfs(8, 8, 3, 3) ➞ 4

### Notes

  * This is a simplified version of [this problem](https://www.spoj.com/problems/NAKANJ/).
  * This travel will always be possible.
  * The chess board is 8x8.

"""

def next_move(x,y):
    for a,b in ((1,2),(2,1)):
        for sx in (1,-1):
            for sy in (1,-1):
                x1, y1 = x + sx*a, y + sy*b
                if all(1 <= z <= 8 for z in (x1,y1)):
                    yield x1, y1
​
def knight_bfs(a,b,c,d):
    start = (a,b)
    end = (c,d)
    if start == end:
        return 0
    st = [start]
    dist_to = {start:0}
    edge_to = {}
    while st:
        pos = st.pop(0)
        for m in next_move(*pos):
            if m == end:
                #path
                # path = [end]
                # edge_to[m] = pos
                # while edge_to[m] != start:
                #     path.append(edge_to[m])
                #     m = edge_to[m]
                # path.append(start)
​
                return dist_to[pos] + 1
            elif m not in dist_to:
                st.append(m)
                dist_to[m] = dist_to[pos] + 1
                edge_to[m] = pos
​
    return -1

