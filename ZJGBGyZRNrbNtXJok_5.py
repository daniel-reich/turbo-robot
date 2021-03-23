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

def nearest_vowel(s):
  x=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  a=s
  y=[]
  o=['a','e','i','o','u']
  d={}
  v=[]
  count=24
  for i in range(len(x)):
    if x[i]==a:
      e=i
      y.append(abs((e+1)-1))
      y.append(abs((e+1)-5))
      y.append(abs((e+1)-9))
      y.append(abs((e+1)-15))
      y.append(abs((e+1)-21))
  for i in range(len(y)):
    d[o[i]]=y[i]
  for i in d.keys():
    if min(d.values())==d.get(i):
      v.append(i)
  return(min(v))

