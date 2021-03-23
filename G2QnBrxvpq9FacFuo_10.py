"""


A floor plan is arranged as follows:

  * Four rooms, which all lead into the hallway.
  * It's impossible to move between rooms without first going into the hallway.

![Room](https://edabit-challenges.s3.amazonaws.com/hdUYysBhbdS.png)

Create a function that validates whether the path between rooms is possible.
The hallway will be given as the letter `"H"`.

### Examples

    possible_path([1, "H", 2, "H", 3, "H", 4]) ➞ True
    
    possible_path(["H", 3, "H"]) ➞ True
    
    possible_path([1, 2, "H", 3]) ➞ False

### Notes

  * A route may begin or end in a hallway.
  * All inputs are either numbers 1-4, or the letter "H".
  * No rooms will repeat.

"""

def possible_path(lst):
  if lst[0]=="H":
    return all(y%2==0 for y,x in enumerate(lst) if x=="H") and all(y%2==1 for y,x in enumerate(lst) if str(x).isdigit())
  else:
    return all(y%2==0 for y,x in enumerate(lst) if str(x).isdigit()) and all(y%2==1 for y,x in enumerate(lst) if x=="H")

