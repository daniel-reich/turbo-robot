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
  if el1 == el2: return 'invalid'
  liAppend = []
  for a in range(0, n + 1, 1):
    if a % 2 == 0: liAppend.append(el1)
    else: liAppend.append(el2)
  li1 = liAppend[:n]
  li2 = liAppend[1:]
  res = []
  for a in range(0, n, 1):
    if a % 2 == 0: res.append(li1)
    else: res.append(li2)
  return res

