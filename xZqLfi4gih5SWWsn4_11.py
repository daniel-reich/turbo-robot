"""


Traveling through Europe one needs to pay attention to how the license plate
in the given country is displayed. When crossing the border you need to park
on the shoulder, unscrew the plate, re-group the characters according to the
local regulations, attach it back and proceed with the journey.

Create a solution that can format the _dmv number_ into a plate number with
correct grouping. The function input consists of string `s` and group length
`n`. The output has to be upper case characters and digits. The new groups are
made from right to left and connected by `-`. The original order of the _dmv
number_ is preserved.

### Examples

    license_plate("5F3Z-2e-9-w", 4) ➞ "5F3Z-2E9W"
    
    license_plate("2-5g-3-J", 2) ➞ "2-5G-3J"
    
    license_plate("2-4A0r7-4k", 3) ➞ "24-A0R-74K"
    
    license_plate("nlj-206-fv", 3) ➞ "NL-J20-6FV"

### Notes

  * You are expected to solve this challenge via a **recursive** approach.
  * An iterative version of this challenge can be found via this [link](https://edabit.com/challenge/HTaZiWnsCGgehpgdr).

"""

def license_plate(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
    
  if (len(Parameters) == 2):
    Parameters.append(0)
    Parameters.append("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    Parameters.append("abcdefghijklmnopqrstuvwxyz")
    Parameters.append("0123456789")
    Parameters.append("")
    Parameters.append(Parameters[0])
  
  Original = Parameters[0]
  Required = Parameters[1]
  Added = Parameters[2]
  Uppers = Parameters[3]
  Lowers = Parameters[4]
  Numbers = Parameters[5]
  Answer = Parameters[6]
  Remaining = Parameters[7]
  
  if (Remaining == ""):
    return Answer
  
  elif (Added == Required):
    Answer = "-" + Answer
    Added = 0
    return license_plate(Original, Required, Added, Uppers, Lowers, Numbers, Answer, Remaining)
  
  elif (Remaining[-1] in Uppers):
    Item = Remaining[-1]
    Answer = Item + Answer
    Added += 1
    Remaining = Remaining[0:-1]
    return license_plate(Original, Required, Added, Uppers, Lowers, Numbers, Answer, Remaining)
  
  elif (Remaining[-1] in Lowers):
    Item = Remaining[-1]
    Answer = Item.upper() + Answer
    Added += 1
    Remaining = Remaining[0:-1]
    return license_plate(Original, Required, Added, Uppers, Lowers, Numbers, Answer, Remaining)
  
  elif (Remaining[-1] in Numbers):
    Item = Remaining[-1]
    Answer = str(Item) + Answer
    Added += 1
    Remaining = Remaining[0:-1]
    return license_plate(Original, Required, Added, Uppers, Lowers, Numbers, Answer, Remaining)
  
  else:
    Remaining = Remaining[0:-1]
    return license_plate(Original, Required, Added, Uppers, Lowers, Numbers, Answer, Remaining)

