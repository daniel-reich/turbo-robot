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

def colour_harmony(anchor,scheme):
    final = []
    colours = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
    dictionary = {"complementary": [0,6],
    "analogous": [-1,0,1],
    "triadic": [4,0,-4],
    "split_complementary": [5,0,-5],
    "rectangle": [2,6,8,0],
    "square": [0,3,6,9]
    }
    
    loop = dictionary[scheme]
    
    for item in loop:
        
        anchor_position = colours.index(anchor)
        
        if item == 0:
            final.append(colours[anchor_position])
        
        if item != 0:
            to_append = anchor_position + item
            if to_append > 11:
                final_append = to_append - 12
                final.append(colours[final_append])
            if to_append < 0:
                final_append = 12 + to_append
                final.append(colours[final_append])
                
            if to_append >= 0 and to_append <= 11:
                final.append(colours[to_append])
    return set(final)

