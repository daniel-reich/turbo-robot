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
    arr = [i for i in range(len(swaps)) if "B" in swaps[i]]
    if not arr: return "B"
    letter = ""
    for i in swaps[arr[0]]:
        if i != "B":
            letter = i
​
    for i in range(len(swaps))[arr[0] + 1:]:
        if letter in swaps[i]:
            for x in swaps[i]:
                if x != letter:
                    letter = x
                    break
    return letter

