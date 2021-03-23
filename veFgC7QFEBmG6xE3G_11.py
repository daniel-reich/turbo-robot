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
  sentence = sentence.lower()
  var = sentence.split()
  a = len(var)
  counter = 0
  for i in range(0, a):
    if i != a - 1:
      c = var[i] [-1]
      d = var[i+1] [0]
      if c == d:
        counter = counter + 1
  return counter == len(var) - 1

