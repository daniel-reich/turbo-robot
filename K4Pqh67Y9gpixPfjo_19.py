"""


ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain
anything but exactly 4 digits or exactly 6 digits. Your task is to create a
function that takes a string and returns `True` if the PIN is valid and
`False` if it's not.

### Examples

    is_valid_PIN("1234") ➞ True
    
    is_valid_PIN("12345") ➞ False
    
    is_valid_PIN("a234") ➞ False
    
    is_valid_PIN("") ➞ False

### Notes

  * Some test cases contain special characters.
  * Empty strings must return `False`.

"""

def is_valid_PIN(pin):
    if (pin.isdigit() and (len(list(pin)) ==4 or len(list(pin)) ==6)):
        return(True)
    else:
        return(False)

