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
    return "invalid"
    
  if n % 2 == 0:
    row1 = [el1, el2] * int(n / 2)
    row2 = [el2, el1] * int(n / 2)
  else:
    row1 = [el1] + ([el2, el1] * int((n - 1) / 2))
    row2 = [el2] + ([el1, el2] * int((n - 1) / 2))
    
  result = []
  for i in range(n):
    if i % 2 == 0:
      result.append(row1)
    else:
      result.append(row2)
  return result
