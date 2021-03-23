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

def checker_board(size:int, El1, El2) -> list:
    
    if El1 == El2: return "invalid"
    
    EV = []
    for x in range(size):
        if x % 2 == 0:
            R1 = list("{0}{1}".format(El1, El2)*(size+1))[0:size]
            if type(El1) == int and type(El2) == int:
                R1 = [int(i) for i in R1]
            EV.append(R1)
        else:
            R1 = list("{1}{0}".format(El1, El2)*(size+1))[0:size]
            if type(El1) == int and type(El2) == int:
                R1 = [int(i) for i in R1]
            EV.append(R1)
        x += 1
    return EV

