"""


Create a function based on the input and output. Look at the examples, there
is a pattern.

### Examples

    secret("p.one.two.three") ➞ "<p class='one two three'></p>"
    
    secret("p.one") ➞ "<p class='one'></p>"
    
    secret("p.four.five") ➞ "<p class='four five'></p>"

### Notes

Input is a string.

"""

def secret(txt):
  s = txt.split('.')
  s1, s2 = s[0], ' '.join(s[1:])
  return "<{0} class='{1}'></{0}>".format(s1,s2)

