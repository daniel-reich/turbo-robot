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
  in_hallway = lst[0] == 'H'
  in_room_1 = lst[0] == 1
  in_room_2 = lst[0] == 2
  in_room_3 = lst[0] == 3
  in_room_4 = lst[0] == 4
  if len(lst) == 1:
    return True
  else:
    for eachroom in lst[1:]:
      # 2 -> 1
      if eachroom == 1 and in_room_2 and not in_room_3 and not in_room_4 and not in_hallway:
        in_room_1 = True
        in_room_2 = False
      # 1 -> 2
      elif eachroom == 2 and in_room_1 and not in_room_2 and not in_room_4 and not in_room_3 and not in_hallway:
        in_room_2 = True
        in_room_1 = False
      #2 -> H
      elif eachroom == 'H' and not in_room_1 and in_room_2 and not in_room_3 and not in_room_4 and not in_hallway:
        in_hallway = True
        in_room_2 = False
      # 4 -> H
      elif eachroom == 'H' and not in_room_1 and not in_room_2 and not in_room_3 and in_room_4 and not in_hallway:
        in_hallway = True
        in_room_4 = False
      # H -> 2
      elif eachroom == 2 and not in_room_1 and not in_room_2 and not in_room_3 and not in_room_4 and in_hallway:
        in_room_2 = True
        in_hallway = False
      # H -> 4
      elif eachroom == 4 and not in_room_1 and not in_room_2 and not in_room_3 and not in_room_4 and in_hallway:
        in_room_4 = True
        in_hallway = False
      #4 -> 3
      elif eachroom == 3 and not in_room_1 and not in_room_2 and not in_room_3 and in_room_4 and not in_hallway:
        in_room_3 = True
        in_room_4 = False
      elif eachroom == 4 and not in_room_1 and not in_room_2 and not in_room_4 and not in_hallway and in_room_3:
        in_room_3 = False
        in_room_4 = True
      else:
        return False
    return True

