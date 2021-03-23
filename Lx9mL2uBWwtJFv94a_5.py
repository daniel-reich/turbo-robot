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

def make_row_odd(n, el1, el2):
  Colcounter = 0
  line = []
  while Colcounter < n:
    if Colcounter % 2 == 0:
      line.append(el1)
    else:
      line.append(el2)
    Colcounter += 1
  return line
​
def make_row_even(n, el1, el2):
  Colcounter = 0
  line = []
  while Colcounter < n:
    if Colcounter % 2 == 0:
      line.append(el2)
    else:
      line.append(el1)
    Colcounter += 1
  return line
  
def build_board(n, el1, el2):
  Rowcounter = 0
  result = []
  while Rowcounter < n:
    if Rowcounter % 2 == 0:
      result.append(make_row_odd(n, el1, el2))
    else:
      result.append(make_row_even(n, el1, el2))
    Rowcounter += 1
  print(result)
  return result
​
def checker_board(n, el1, el2):
  if el1 == el2:
    return "invalid"
  else:
    return build_board(n, el1, el2)

