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

def percent_filled(array):
    free_blocks, filled_blocks = 0,0
    for i in array:
        for e in range(0,len(i),1):
            if i[e] != "#":
                free_blocks += 1
            if i[e] != "#" and i[e] != " ":
                filled_blocks += 1
    return "{}%".format(int((int(filled_blocks)/int(free_blocks))*100))

