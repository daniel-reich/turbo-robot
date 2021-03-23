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
    if len(ldr[0])<5:
        return False           # not a ladder or too short
    # since i don't need top and bottom element, they are removed
    ldr.pop(0), ldr.pop(-1)
    # broken rung
    if any(Z.count('#') in range(3, len(ldr[0])) for Z in ldr):
        return False      
    # calculate distance between rungs
    lw = list(enumerate([1 if all(Z=='#' for Z in Y) else 0 for Y in ldr]))
    # only rungs with position
    lw2 = [Z for Z in lw if Z[1] == 1]
    # no rungs
    if len(lw2)==0:
        return False
    d0 = lw2[1][0]-lw2[0][0]
    # if distance between rungs is greated than 3, 
    # or spaces between them are greater than 2
    if d0 > 3:
        return False
    # calculate equidistance
    for i in range(2,len(lw2)):
        if lw2[i][0] - lw2[i-1][0] != d0:
            return False
    return True

