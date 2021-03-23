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
  ret_string = ''
  for letter in txt:
    if letter.isupper():
      ret_string += ' ' + letter
    else:
      ret_string += letter
  return ret_string.lower()

