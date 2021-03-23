"""


When coloring a striped pattern, you may start by coloring each square
_sequentially_ , meaning you spend time needing to _switch coloring pencils_.

Create a function where given a _list of colors_ `cols`, return how long it
takes to color the whole pattern. Note the following times:

  * It takes **1 second** to _switch between pencils_.
  * It takes **2 seconds** to _color a square_.

See the example below for clarification.

    color_pattern_times(["Red", "Blue", "Red", "Blue", "Red"]) ➞ 14
    
    # There are 5 colors so it takes 2 seconds to color each one (2 x 5 = 10).
    # You need to switch the pencils 4 times and it takes 1 second to switch (1 x 4 = 4).
    # 10 + 4 = 14

### Examples

    color_pattern_times(["Blue"]) ➞ 2
    
    color_pattern_times(["Red", "Yellow", "Green", "Blue"]) ➞ 11
    
    color_pattern_times(["Blue", "Blue", "Blue", "Red", "Red", "Red"]) ➞ 13

### Notes

  * Only change coloring pencils if the next color is different to the color before it.
  * Return a number in _seconds_.

"""

def color_pattern_times(cols):
  return len(cols)*2 + sum([1 for x in range(0, len(cols)-1) if cols[x] != cols[x+1]])

