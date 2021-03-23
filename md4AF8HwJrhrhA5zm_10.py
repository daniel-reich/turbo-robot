"""


In colour theory, colour _harmony_ refers to an aesthetically pleasing
combination of colours. The standard colour wheel shows the 12 primary,
secondary and tertiary colours. Starting with _red_ , and moving clockwise,
the colours are:

    colours = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]

With an initial colour (called the **anchor** ), you can find combinations of
harmonious colours. The combination types are shown below, for an anchor
colour of _green_ :

![Image of Colour Combinations](https://edabit-
challenges.s3.amazonaws.com/colour_harmony.png)

Given an anchor colour and a combination type, write a function that returns a
_set_ containing all colours within the combination.

### Examples

    colour_harmony("green", "triadic") ➞ { "green", "violet", "orange" }
    
    colour_harmony("blue-green", "complementary") ➞ { "blue-green", "red-orange" }
    
    colour_harmony("orange", "analogous") ➞ { "yellow-orange", "red-orange", "orange" }

### Notes

  * Create the combinations given their relative positions from the anchor colour. For example, the rectangle combination starts with the colours two positions clockwise and four positions anti-clockwise from the anchor (and not the other way around). With the split-complemetary combination, you take the colours five positions both clockwise and anti-clockwise from the anchor. For the analogous combination, you include the colours directly on either side of the anchor.
  * Include the anchor colour in the final set.

"""

def colour_harmony(anchor, c):
  colours=["red","red-orange","orange","yellow-orange","yellow","yellow-green"]
  colours+=["green","blue-green","blue","blue-violet","violet","red-violet"]
  
  combs = {}
  combs["complementary"] = [0,6]
  combs["analogous"] = [0,1,-1]
  combs["split_complementary"] = [0,5,-5]
  combs["triadic"] = [0,4,-4]
  combs["rectangle"] = [0,2,6,-4]
  combs["square"] = [0,3,6,-3]
  
  r = colours.index(anchor)
  return {colours[(r+i)%12] for i in combs[c]}

