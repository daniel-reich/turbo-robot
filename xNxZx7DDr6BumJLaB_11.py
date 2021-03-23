"""


 **Mubashir** wants to remove numbers from a given string!

Help him by fixing the code in the code tab to pass this challenge. Look at
the examples below to get an idea of what the function should do.

### Examples

    remove_numbers("mubashir1") ➞ "mubashir"
    
    remove_numbers("12ma23tt") ➞ "matt"
    
    remove_numbers("e1d2a3b4i5t6") ➞ "edabit"

### Notes

  *  **READ EVERY WORD CAREFULLY, CHARACTER BY CHARACTER!**
  * Don't overthink this challenge; it's not supposed to be hard.

"""

def remove_numbers(string):
  chars = list(string)
  print(chars)
  letters = []
  for char in chars:
    print(char)
    try: int(char)
    except: letters.append(char)
    
  return "".join(letters)

