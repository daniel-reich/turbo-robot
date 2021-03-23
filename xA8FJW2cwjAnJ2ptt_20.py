"""


Create a function that finds the word `"bomb"` in the given string. If found,
return `"Duck!!!"`, otherwise, return `"There is no bomb, relax."`.

### Examples

    bomb("There is a bomb.") ➞ "Duck!!!"
    
    bomb("Hey, did you think there is a bomb?") ➞ "Duck!!!"
    
    bomb("This goes boom!!!") ➞ "There is no bomb, relax."

### Notes

`"bomb"` may appear in different cases (i.e. uppercase, lowercase, mixed).

"""

def bomb(txt):
  a = txt.lower()
  if 'bomb' in a:
    return 'Duck!!!'
  else:
    return "There is no bomb, relax."

