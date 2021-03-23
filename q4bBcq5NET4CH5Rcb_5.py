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

valueDict = {
  "half": 0.5,
  "quarter": 0.25,
  "eighth": 1/8,
  "sixteenth": 1/16
}
  
def jay_and_bob(txt):
  result = 0
  for value in valueDict:
    if txt == value:
      result = 28*valueDict[value]
      if (result).is_integer():
        result = int(result)
  result = str(result)
  return(result + " grams")

