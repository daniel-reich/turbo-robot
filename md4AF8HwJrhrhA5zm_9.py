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

def colour_harmony(anchor, combination):
    lst = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
    pos = lst.index(anchor)
    comp = (pos+len(lst)//2)%len(lst)
    
    if combination == 'complementary':
        return {anchor, lst[comp]}
    if combination == 'split_complementary':
        return {anchor, lst[(comp+1)%len(lst)], lst[(comp-1)%len(lst)]}
    if combination == 'analogous':
        return {anchor, lst[pos+1%len(lst)], lst[pos-1%len(lst)]}
    if combination == 'square':
        return {lst[comp], lst[(comp-3)%len(lst)], lst[(comp+3)%len(lst)], anchor}
    if combination == 'triadic':
        return {anchor, lst[(comp+2)%len(lst)], lst[(comp-2)%len(lst)]}
    if combination == 'rectangle':
        return {lst[comp], lst[(comp+2)%len(lst)], lst[(pos+2)%len(lst)], anchor}

