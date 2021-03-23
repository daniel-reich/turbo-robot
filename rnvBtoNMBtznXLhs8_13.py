"""


You have a pack of 5 randomly numbered cards, which can range from 0-9. You
can win if you can produce a higher **two-digit** number from your cards, than
your opponent. Return `True` if your cards win that round.

### Worked Example

    win_round([2, 5, 2, 6, 9], [3, 7, 3, 1, 2]) ➞ True
    # Your cards can make the number 96
    # Your opponent can make the number 73
    # You win the round since 96 > 73

### Examples

    win_round([2, 5, 2, 6, 9], [3, 7, 3, 1, 2]) ➞ True
    
    win_round([1, 2, 3, 4, 5], [9, 8, 7, 6, 5]) ➞ False
    
    win_round([4, 3, 4, 4, 5], [3, 2, 5, 4, 1]) ➞ False

### Notes

Return `False` if you and your opponent reach the same maximum number (see
example #3).

"""

def win_round(you, opp):
  v=sorted(you)
  u=sorted(opp)
  m=str(v[-1])+str(v[-2])
  n=str(u[-1])+str(u[-2])
  return int(m)>int(n)

