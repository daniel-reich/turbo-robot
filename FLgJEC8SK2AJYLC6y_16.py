"""


A floor plan is arranged as follows:

  * You may freely move between rooms 1 and 2.
  * You may freely move between rooms 3 and 4.
  * However, you can enter the hallway to move between rooms 2 and 4.

![Floor Plan](https://edabit-challenges.s3.amazonaws.com/sNdBGbbhbdjdn.png)

Create a function that validates whether the route taken between rooms is
possible. The hallway will be given as the letter `"H"`.

### Examples

    possible_path([1, 2, "H", 4, 3]) ➞ True
    
    possible_path(["H", 1, 2]) ➞ False
    
    possible_path([4, 3, 4, "H", 4, "H"]) ➞ True

### Notes

  * A route may begin or end in any room (including the hallway).
  * All inputs are either numbers 1-4 or the letter "H".
  * No rooms will repeat.

"""

def possible_path(lst):
  for i in range(len(lst)-1):
    if lst[i] == 1:
      if lst[i+1] != 2:
        return False
    if lst[i] == 2:
      if lst[i+1] not in (1,'H'):
        return False
    if lst[i] == 'H':
      if lst[i+1] not in (2,4):
        return False
    if lst[i] == 4:
      if lst[i+1] not in ('H',3):
        return False
    if lst[i] == 3:
      if lst[i+1] != 4:
        return False
  return True

