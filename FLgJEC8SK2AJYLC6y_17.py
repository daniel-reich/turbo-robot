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
  doors = ["12", "34", "2H", "4H"]
  pairs = []
  for i, room in enumerate(lst):
    if i == 0:
      continue
    pairs.append("".join(sorted(str(room)+str(lst[i-1]))))
  for pair in pairs:
    if not pair in doors:
      return False
  return True

