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

def knight_bfs(a, b, c, d):
  start,end=(a,b),(c,d)
  if start == end:
    return(0)
  piece_moves=[(1,2),(1,-2),(-2,1),(-2,-1),(-1,2),(-1,-2),(2,1),(2,-1)]
  new_pos =(start[0],start[1])
  distance =((start[0]-end[0])**2 + (start[1]-end[1])**2)**.5
  i, min_distance=0,10
  while not (min_distance ==0 or i > 100):
    min_distance = 10
    for piece in piece_moves:
      if (new_pos[0]+piece[0]>0 and new_pos[1]+piece[1]>0 and new_pos[0]+piece[0]<9 and new_pos[1]+piece[1]<9):
        distance =((new_pos[0]+piece[0]-end[0])**2 + (new_pos[1]+piece[1]-end[1])**2)**.5
        horizontal_distance,vertical_distance= abs(new_pos[0]+piece[0]-end[0]),abs(new_pos[1]+piece[1]-end[1])
        if horizontal_distance+vertical_distance>2 or horizontal_distance+vertical_distance==0 or (horizontal_distance==0 and vertical_distance==2) or (horizontal_distance==2 and vertical_distance==0):
          if distance < min_distance:
            if (horizontal_distance == vertical_distance and distance >0):
              if(distance > 8**0.5):
                curr_pos=(new_pos[0]+piece[0],new_pos[1]+piece[1])
                min_distance=distance
            else:
              curr_pos=(new_pos[0]+piece[0],new_pos[1]+piece[1])
              min_distance=distance
    new_pos = curr_pos
    i+=1
  return i

