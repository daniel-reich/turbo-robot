"""


Create a function that accepts a string and returns `True` if it's in the
format of a proper phone number and `False` if it's not. Assume any number
between 0-9 (in the appropriate spots) will produce a valid phone number.

This is what a valid phone number looks like:

    (123) 456-7890

### Examples

    is_valid_phone_number("(123) 456-7890") ➞ True
    
    is_valid_phone_number("1111)555 2345") ➞ False
    
    is_valid_phone_number("098) 123 4567") ➞ False

### Notes

Don't forget the space after the closing parentheses.

"""

def is_valid_phone_number(txt):
  a=len(txt)
  if(a!=14):
    return False
  else:
    if(txt[0]!="(" or txt[4]!=")" or txt[5]!=" " or txt[9]!="-"):
      return False
  return True

