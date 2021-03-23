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
  par1 = txt.find('(')
  par2 = txt.find(')')
  dash = txt.find('-')
  space = txt.find(' ')
  if(par1 == 0 and par2 == 4 and dash == 9 and space == 5 and len(txt) == 14):
      return True
  return False

