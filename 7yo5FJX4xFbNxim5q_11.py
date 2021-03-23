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
  letter_count = 0
  letter_count_alt = 0
  po_length = len(po)
  last_po_length = len(po[po_length-1])   
  if po_length == 1 and last_po_length == 0:
    return -1
  elif po_length == 1:
    return sum(po[0])
  else:
    for i in range(po_length-1):
      letter_count = letter_count + po[i][0]
    for j in range(last_po_length):
      letter_count = letter_count + po[last_po_length-1][j]
    for j in range(last_po_length-1):
      letter_count_alt = letter_count_alt + po[0][j]
    for i in range(po_length):
      letter_count_alt = letter_count_alt + po[i][last_po_length-1]
    return max(letter_count, letter_count_alt)

