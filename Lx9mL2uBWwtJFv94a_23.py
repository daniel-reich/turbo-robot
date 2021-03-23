"""


Create a **checker board generator** , which takes as inputs `n` and `2
elements` to generate an `n x n` checkerboard with those two elements as
alternating squares.

### Examples

    checker_board(2, 7, 6) ➞ [
      [7, 6],
      [6, 7]
    ]
    
    checker_board(3, "A", "B") ➞ [
      ["A", "B", "A"],
      ["B", "A", "B"],
      ["A", "B", "A"]
    ]
    
    checker_board(4, "c", "d") ➞ [
      ["c", "d", "c", "d"],
      ["d", "c", "d", "c"],
      ["c", "d", "c", "d"],
      ["d", "c", "d", "c"]
    ]
    
    checker_board(4, "c", "c") ➞ "invalid"

### Notes

  * Both elements can be either strings or integers.
  * The first element should be on the upper left corner of the checker board. e.g. "c", not "d" should be element `[0][0]` for example 3.
  * Return "invalid" if both inputs are identical (see example 4).

"""

def checker_board(n, el1, el2):
  if el1 == el2:
    return 'invalid'
  output = []
  lsteven = []
  while len(lsteven) < n:
    lsteven.append(el1)
    if len(lsteven) == n:
      break
    lsteven.append(el2)
  lstodd = []
  while len(lstodd) < n:
    lstodd.append(el2)
    if len(lstodd) == n:
      break
    lstodd.append(el1)
  for i in range(n):
    if i% 2 == 0:
      output.append(lsteven)
    else:
      output.append(lstodd)
  return output

