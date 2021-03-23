"""


Jay and Silent Bob have been given a fraction of an ounce but they only
understand grams. Convert a fraction passed as a string to grams with up to
two decimal places. An ounce weighs 28 grams.

### Examples

    jay_and_bob("half") ➞ "14 grams"
    
    jay_and_bob("quarter") ➞ "7 grams"
    
    jay_and_bob("eighth") ➞ "3.5 grams"

### Notes

Add the string "grams" to the end with a space.

"""

def jay_and_bob(txt):
  d = {"half": .5, "quarter": .25, "eighth": .125, "sixteenth": .0625}
  num = str(round(28 * d[txt], 2))
  return "{} grams".format(num.split(".")[0] if num.endswith(".0") else num)

