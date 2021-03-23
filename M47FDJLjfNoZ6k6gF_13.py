"""


There are three cups on a table, at positions **A, B, and C.** At the start,
there is a ball hidden under the cup at **position B**.

![Image of cups where ball is under middle cup](https://edabit-
challenges.s3.amazonaws.com/kfnerNJDNn.png)

However, I perform several swaps on the cups, which is notated as two letters.
For example, if I swap the cups at positions **A and B** , I could notate this
as `AB` or `BA`.

Create a function that returns the letter position that the ball is at, once I
finish swapping the cups. The swaps will be given to you as a list.

### Worked Example

    cup_swapping(["AB", "CA", "AB"]) ➞ "C"
    
    # Ball begins at position B.
    # Cups A and B swap, so the ball is at position A.
    # Cups C and A swap, so the ball is at position C.
    # Cups A and B swap, but the ball is at position C, so it doesn't move.

### Examples

    cup_swapping(["AB", "CA"]) ➞ "C"
    
    cup_swapping(["AC", "CA", "CA", "AC"]) ➞ "B"
    
    cup_swapping(["BA", "AC", "CA", "BC"]) ➞ "A"

### Notes

  * A swap could be notated in two different ways, since both ways end up with the same outcome.
  * All swaps will be notated as capital letters and will be valid.
  * You cannot swap a cup with itself.

"""

def cup_swapping(swaps):
  positions = ['A','B','C']
  position_number = 1
  for eachswap in swaps:
    #position 1
    if 'A' in eachswap and 'B' in eachswap and position_number == 1:
      position_number = 0
    elif 'C' in eachswap and 'B' in eachswap and position_number == 1:
      position_number = 2
    #position 2
    elif 'B' in eachswap and 'C' in eachswap and position_number == 2:
      position_number = 1
    elif 'A' in eachswap and 'C' in eachswap and position_number == 2:
      position_number = 0
    #position 0
    elif 'B' in eachswap and 'A' in eachswap and position_number == 0:
      position_number = 1
    elif 'C' in eachswap and 'A' in eachswap and position_number == 0:
      position_number = 2
  return positions[position_number]

