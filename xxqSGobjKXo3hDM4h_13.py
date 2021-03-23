"""


Write a function that takes a string as an argument and returns a list of all
the words inflected by "-ing". Your function should also exclude all the mono-
syllabic words ending in "-ing" (e.g. bing, sing, sling, ...). Although these
words end in "-ing", the "-ing" is not an inflection affix.

### Examples

    ing_extractor("coming bringing Letting sing") ➞ ["coming", "bringing", "Letting"]
    
    ing_extractor("going Ping, king sHrink dOing") ➞ ["going",, "dOing"]
    
    ing_extractor("zing went ring, ding wing SINk") ➞ []

### Notes

  * Mono-syllabic means the word must include two or more of the letters a, e, i, o, u.
  * It's probably best to use RegEx for this challenge.

"""

def ing_extractor(string):
  a="abcdefghijklmnopqrstuvwxyz"
  b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  f=[]
  v=""
  s=string.split()
  for d in range(len(s)):
    for r in range(len(s[d])):
      if s[d][r] in a or s[d][r] in b or s[d][r]=="*":
        v=v+s[d][r]
    s[d]=v
    v=""
  for e in s:
    if e[len(e)-3:len(e)].lower()=="ing":
      if "o" in e[0:len(e)-3].lower() or "a" in e[0:len(e)-3].lower() or "e" in e[0:len(e)-3].lower() or "i" in e[0:len(e)-3].lower() or "u" in e[0:len(e)-3].lower() or "*" in e[0:len(e)-3].lower():
        f.append(e)
  return f

