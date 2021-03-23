"""


Given a letter, created a function which returns the nearest vowel to the
letter. If two vowels are equidistant to the given letter, return the
_earlier_ vowel.

### Examples

    nearest_vowel("b") ➞ "a"
    
    nearest_vowel("s") ➞ "u"
    
    nearest_vowel("c") ➞ "a"
    
    nearest_vowel("i") ➞ "i"

### Notes

  * All letters will be given in lowercase.
  * There will be no alphabet wrapping involved, meaning the closest vowel to "z" should return "u", not "a".

"""

def dist(v, s):
  return abs(ord(v) - ord(s))
​
def nearest_vowel(s):
  vol = "aeiou"
  
  if s in vol:
    return s
    
  res = []
  
  start = ord(s)
​
  for i in range(start, ord('a')-1, -1):
    i = chr(i)
    if i in vol:
       res.append(i)
       break
  
  for i in range(start, ord('z')+1, 1):
    i = chr(i) 
    if i in vol:
       res.append(i)
       break
​
  if len(res) < 2:
    return res[0]
  
  dist1, dist2 = dist(res[0], s), dist(res[1], s)
  
  if dist1 == dist2:
    return res[0] if ord(res[0]) < ord(res[1]) else res[1]
  else:
    return res[0] if dist1 < dist2 else res[1]

