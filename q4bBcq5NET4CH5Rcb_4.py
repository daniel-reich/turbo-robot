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
  conversion=28
  switch={"half":conversion/2,
  "third":conversion/3,
  "quarter":conversion/4,
  "fifth":conversion/5,
  "seventh":conversion/7,
  "sixth":conversion/6,
  "eighth":conversion/8,
  "sixteenth": conversion/16}
  if switch.get(txt)%1 == 0:
    return  str((int)(switch.get(txt)))+" grams"
  return  str(switch.get(txt))+" grams"

