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

frac_dict = {
    'half': 2,
    'quarter': 4,
    'eighth': 8,
    'sixteenth': 16
  }
def jay_and_bob(txt):
  calc = 28 % frac_dict[txt]
  if not calc:
    return str(28 // frac_dict[txt]) + ' grams'
  else:
    return str(28 / frac_dict[txt]) + ' grams'

