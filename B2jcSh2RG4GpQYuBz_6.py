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
  fb = txt[1:4]
  sb = txt[6:9]
  tb = txt[10:]
  if len(txt)==14:
    if txt[0]=="(" and txt[4]==")":
      if txt[5]==" " and txt[9]=="-":
        if fb.isdigit()==True and sb.isdigit()==True and tb.isdigit()==True:
          return True
  return False

