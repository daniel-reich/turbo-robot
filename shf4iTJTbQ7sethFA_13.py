"""


There are two players, Alice and Bob, each with a 3-by-3 grid. A referee tells
Alice to fill out one particular row in the grid (say the second row) by
putting either a 1 or a 0 in each box, such that the sum of the numbers in
that row is odd. The referee tells Bob to fill out one column in the grid (say
the first column) by putting either a 1 or a 0 in each box, such that the sum
of the numbers in that column is even.

Alice and Bob win the game if Alice’s numbers give an odd sum, Bob’s give an
even sum, and ( **most important** ) they’ve each written down the same number
in the one square where their row and column intersect.

### Examples

    magic_square_game([2, "100"], [1, "101"]) ➞ False
    
    magic_square_game([2, "001"], [1, "101"]) ➞ True
    
    magic_square_game([3, "111"], [2, "011"]) ➞ True
    
    magic_square_game([1, "010"], [3, "101"]) ➞ False
    
    # Two lists, Alice [row, "her choice"], Bob [column, "his choice"]

### Notes

  * Look at the article in the **resources tab** to see the first two examples in action.
  * The **row** of Alice is always **odd** , the **column** of Bob is always **even**.

"""

def magic_square_game(alice, bob):
  return alice[1][bob[0]-1]==bob[1][alice[0]-1]

