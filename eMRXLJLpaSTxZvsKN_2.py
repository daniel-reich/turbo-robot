"""


Due to a huge scandal about the _Laddersons Ladder Factory_ creating faulty
ladders, the _Occupational Safety and Health Administration_ require your help
in determining whether a ladder is safe enough for use in the work place! It
is vital that a ladder passes all criterea:

  * The ladder must be at least **5 characters wide**.
  * The ladder mustn't have more than a **2 character gap** _between rungs_.
  * Rungs must be **evenly spaced apart**.
  * Rungs should not be broken (i.e. **no gaps** ).

Given a ladder (drawn as a _list of strings_ ) return `True` if it passes
**all** of OSHA's criterea.

### Examples

    is_ladder_safe([
      "#   #",
      "#####",
      "#   #",
      "#   #",
      "#####",
      "#   #",
      "#   #",
      "#####",
      "#   #"
    ]) ➞ True
    is_ladder_safe([
      "#   #",
      "#####",
      "#   #",
      "#####",
      "#   #",
      "#   #",
      "#####",
      "#   #"
    ]) ➞ False
    
    # Uneven spaces between rungs.
    is_ladder_safe([
      "#  #",
      "####",
      "#  #",
      "#  #",
      "####",
      "#  #",
      "#  #",
      "####",
      "#  #"
    ]) ➞ False
    
    # Ladder is too narrow, should be at least 5 characters wide.
    is_ladder_safe([
      "#   #",
      "#####",
      "#   #",
      "#   #",
      "#   #",
      "#   #",
      "#####",
      "#   #",
      "#   #",
      "#   #",
      "#   #",
      "#####",
      "#   #"
    ]), ➞ False
    
    # Gap between rungs is too wide, should be less than 3.
    is_ladder_safe([
      "#   #",
      "#  ##",
      "#   #",
      "#   #",
      "#####",
      "#   #",
      "#   #",
      "#####",
      "#   #"
    ]) ➞ False
    
    # The top rung is broken.

### Notes

  * There will be a one character space with _no rung_ at the top and bottom of every ladder.
  * The height of the ladder is not needed for solving this problem.

"""

def is_ladder_safe(ldr):
  n = len(ldr[0])
  if n >= 5:
    rung = '#'*n
    not_rung = '#' + ' '*(n-2) + '#'
    if all(row in [rung,not_rung] for row in ldr):
      rungs = [i for i in range(len(ldr)) if ldr[i] == rung]
      gap = [b-a for a, b in zip(rungs,rungs[1:])]
      return len(set(gap)) == 1 and gap[0] <= 3
  return False

