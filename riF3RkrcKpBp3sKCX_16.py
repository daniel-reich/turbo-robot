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
  indices = []
  for i in range (len(txt)):
    if txt[i].isupper():
     txt = (txt[:i]) + (txt[i].lower()) + (txt[(i+1):])
     indices.append(i)
  print (indices)
  for j in indices:
    txt = (txt[:j])+" "+(txt[j:])
    for k in range (len(indices)):
      indices[k]= indices[k]+1
  return (txt)

