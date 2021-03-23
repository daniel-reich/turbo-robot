"""


Harry is a postman. He's got a post office with a size of `n*m(a matrix / 2D
list)`. Each slot at the 2D list represents the number of letters in that
spot. Harry can only go right and down. He starts at (0, 0), and ends at (n-1,
m-1). `n` represents the height, and `m` the length. Return the maximum amount
of letters he can pick up. He can only pick up letters if he is on that spot.

### Examples

    harry([[5, 2], [5, 2]]) ➞ 12
    # (5+5+2)
    harry([
      [1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10],
      [11, 12, 13, 14, 15]
    ]) ➞ 72
    # (1+6+11+12+13+14+15)
    harry([[]]) ➞ -1

### Notes

Like you saw in example 3, if the matrix is empty, return `-1`.

"""

def harry(po):
    newlist = []
    total = 0
    if len(po[0]) == 0:
        return -1
    if len(po[0]) == 1:
        return sum(po[0])
    else:
        ### get right down right down
        end_point = (len(po)-1,len(po[0])-1)
        #first combo all the way right then all the way down
        first_right = sum(po[0])
        total += first_right
        for i in range(1,len(po)):
            total += po[i][-1]
        newlist.append(total)
        total = 0
        last_row = po[len(po)-1][1:]
        for i in range(len(po)):
            total += po[i][0]
        total += sum(last_row)
        newlist.append(total)
        return max(newlist)

