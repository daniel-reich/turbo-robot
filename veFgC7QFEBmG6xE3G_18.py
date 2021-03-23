"""
Carlos is a huge fan of something he calls **smooth sentences**.

A smooth sentence is one where the last letter of each word is identical to
the first letter the following word (and not case sensitive, so "A" would be
the same as "a").

The following would be a smooth sentence _"Carlos swam masterfully"_ because
"Carlos" ends with an "s" and swam begins with an "s" and swam ends with an
"m" and masterfully begins with an "m".

Create a function that determines whether the input sentence is a smooth
sentence, returning a boolean value `True` if it is, `False` if it is not.

### Examples

    is_smooth("Marta appreciated deep perpendicular right trapezoids") ➞ True
    
    is_smooth("Someone is outside the doorway") ➞ False
    
    is_smooth("She eats super righteously") ➞ True

### Notes

  * The last and first letters are case insensitive.
  * There will be no punctuation in each sentence.

"""

def is_smooth(sentence):
  l = sentence.split()
  
  for x in range(1, len(l)-1):
    if l[x][0].lower() != l[x-1][-1].lower(): return False
  return True

