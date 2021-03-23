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
    brd = [list(i) for i in lst]; row = len(brd); col = len(brd[0])
    num = sorted([j for i in brd for j in i if j != '0'])
​
    pos = {}
    for i in num:
        pos[i] = ()
​
    for i in range(row):
        for j in range(col):
            if brd[i][j] in pos:
                pos[brd[i][j]] = (i, j)
​
    dic = sorted(pos.items(), key = lambda x: x[0][0])
    fin = [dic[i][1] for i in range(len(dic))]
​
    dis = []
    for i in range(len(fin)-1):
        dis.append(abs(fin[i][0]-fin[i+1][0]))
        dis.append(abs(fin[i][1]-fin[i+1][1]))
​
    return sum(dis)

