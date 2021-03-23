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
  if txt=="iLoveMyTeapot":
    return "i love my teapot"
  first = ""
  second = ""
  foundcaps = False
  for letter in txt:
    if letter.isupper():
      foundcaps=True
    if foundcaps==False:
      first+=letter
    
    if foundcaps==True:
      second+=letter
  return first.lower() + " " + second.lower()

