"""


Create a function that takes a string of words (or just one word) and converts
each word from camelCase to snake_case.

### Examples

    camel_to_snake("magicCarrots") ➞ "magic_carrots"
    
    camel_to_snake("greatApples for aSmellyRhino") ➞ "great_apples for a_smelly_rhino"
    
    camel_to_snake("thatsGreat") ➞ "thats_great"

### Notes

You won't get more than two capitals in a row (e.g. `"DIYFoods"` is not
given).

"""

def camel_to_snake(s):
  output = ""
  for i in range(0,len(s)-1): 
    if s[i+1].isupper():
      output+=s[i]+'_'
      i+=2
    else:
      if s[i].islower():
        output+=s[i]
      else:
        output+=s[i].lower()
  
  return output+s[-1]

