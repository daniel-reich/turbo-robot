"""


Create a function that calculates what percentage of the box is filled in.
Give your answer as a string percentage rounded to the nearest integer.

### Examples

    percent_filled([
      "####",
      "#  #",
      "#o #",
      "####"
    ]) ➞ "25%"
    
    # One element out of four spaces.
    
    percent_filled([
      "#######",
      "#o oo #",
      "#######"
    ]) ➞ "60%"
    
    # Three elements out of five spaces.
    
    percent_filled([
      "######",
      "#ooo #",
      "#oo  #",
      "#    #",
      "#    #",
      "######"
    ]) ➞ "31%"
    
    # Five elements out of sixteen spaces.

### Notes

  * Only "o" will fill the box and also "o" will not be found outside of the box.
  * Don't focus on how much physical space an element takes up, pretend that each element occupies one whole unit (which you can judge according to the number of "#" on the sides).

"""

def percent_filled(box):
    ttl_spaces,ttl_filled = 0,0
    for row in box:
        spaces = len([i for i in row if i != "#"])
        filled = len([i for i in row if i == "o"])
        ttl_spaces += spaces
        ttl_filled += filled
    if ttl_filled:
        return str(round((ttl_filled/ttl_spaces)*100))+"%"
    return "0%"
