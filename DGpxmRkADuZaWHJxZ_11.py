"""


Steve and Maurice have racing snails. They each have three, a slow `s`, medium
`m` and fast `f` one. Although Steve's snails are all a bit stronger than
Maurice's, Maurice has a trick up his sleeve. His plan is:

  1. Round 1: `[s, f]` Sacrifice his slowest snail against Steve's fastest.
  2. Round 2: `[m, s]` Use his middle snail against Steve's slowest.
  3. Round 3: `[f, m]` Use his fastest snail against Steve's middle.

Create a function that determines whether Maurice's plan will work by
outputting `True` if Maurice wins 2/3 games.

The function inputs:

  1. List 1: `[s, m, f]` for Maurice.
  2. List 2: `[s, m, f]` for Steve.

### Examples

    maurice_wins([3, 5, 10], [4, 7, 11]) ➞ True
    # Since the matches are (3, 11), (5, 4) and (10, 7), Maurice wins 2 out of 3.
    
    maurice_wins([6, 8, 9], [7, 12, 14]) ➞ False
    # Since the matches are (6, 14), (8, 7) and (9, 12), Steve wins 2 out of 3.
    
    maurice_wins([1, 8, 20], [2, 9, 100]) ➞ True

### Notes

  * Maurice wins if his competing snail's speed **strictly** exceeds Steve's snail's speed.
  * Steve will always play in this order: `[f, s, m]`.
  * The order you'll get the snails is always in ascending order.

"""

def maurice_wins(m_snails, s_snails):
    return sum(m_snails[1:][n] > s_snails[n] for n in range(2)) == 2

