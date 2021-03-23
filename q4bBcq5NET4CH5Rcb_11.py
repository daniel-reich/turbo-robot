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
  if txt == 'half':
    return str(28 // 2) + ' grams'
  elif txt == 'quarter':
    return str(28 // 4) + ' grams'
  elif txt == 'eighth':
    return str(round(28 / 8,2)) + ' grams'
  elif txt == 'sixteenth':
    return str(round(28 / 16,2)) + ' grams'
  else:
    return "invalid"

