"""


Create a function which adds spaces before every capital in a word.
Uncapitalize the whole string afterwards.

### Examples

    cap_space("helloWorld") ➞ "hello world"
    
    cap_space("iLoveMyTeapot") ➞ "i love my teapot"
    
    cap_space("stayIndoors") ➞ "stay indoors"

### Notes

The first letter will stay uncapitalized.

"""

def cap_space(txt):
  ss = map(str, txt.strip())
  res = []
  i = 0
  for elem in ss:
    if(i!= 0):
      if(elem.isupper()):
        res.append(' ')
        res.append(elem.lower())
      else:
        res.append(elem)
    else:
      res.append(elem)
    i += 1
    
  r = ""
  for elem in res:
    r += str(elem)
  return r

