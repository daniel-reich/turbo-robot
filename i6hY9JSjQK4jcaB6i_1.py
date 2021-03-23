"""


Create a function that inverts the `rgb` values of a given tuple.

### Examples

    color_invert((255, 255, 255)) ➞ (0, 0, 0)
    # (255, 255, 255) is the color white.
    # The opposite is (0, 0, 0), which is black.
    
    color_invert((0, 0, 0)) ➞ (255, 255, 255)
    
    color_invert((165, 170, 221)) ➞ (90, 85, 34)

### Notes

  * Must return a tuple.
  * 255 is the max value of a single color channel.

"""

def color_invert(rgb):
    r, g, b = rgb
    return (255-r, 255-g, 255-b)

