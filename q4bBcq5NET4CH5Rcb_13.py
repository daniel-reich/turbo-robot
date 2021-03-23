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
  if txt == "half":
    return("{0} {1}".format('14', 'grams'))
  if txt == "quarter":
    return("{0} {1}".format('7', 'grams'))
  if txt == "eighth":
    return("{0} {1}".format('3.5', 'grams'))  
  if txt == "sixteenth":
    return("{0} {1}".format('1.75', 'grams'))

