"""


For this exercise, keep in mind the following two terms (mutually exclusive):

  1.  **initials** = 1 character
  2.  **words** = 2+ characters (no dots allowed)

A **valid name** is a name written in one of the following ways:

  * H. Wells
  * H. G. Wells
  * Herbert G. Wells
  * Herbert George Wells

The following names are **invalid** :

  * Herbert or Wells (single names not allowed)
  * H Wells or H. G Wells (initials must end with dot)
  * h. Wells or H. wells or h. g. Wells (incorrect capitalization)
  * H. George Wells (middle name expanded, while first still left as initial)
  * H. G. W. (last name is not a word)
  * Herb. G. W. (dot only allowed after initial, not word)

### Rules

  1. Both initials and words must be capitalized.
  2. Initials must end with a dot.
  3. A name must be either 2 or 3 words long (depending on whether a middle name exists).
  4. If the name is 3 words long, you can expand the first and middle name or expand the first name only. You **cannot** keep the first name as an initial and expand the middle name only.
  5. The last name must be a word (not an initial).

Your task is to write a function that determines whether a name is valid or
not. Return `True` if the name is valid, `False` otherwise.

### Examples

    valid_name("H. Wells") ➞ True
    
    valid_name("H. G. Wells") ➞ True
    
    valid_name("Herbert G. Wells") ➞ True
    
    valid_name("Herbert") ➞ False
    # Must be 2 or 3 words
    
    valid_name("h. Wells") ➞ False
    # Incorrect capitalization
    
    valid_name("H Wells") ➞ False
    # Missing dot after initial
    
    valid_name("H. George Wells") ➞ False
    # Cannot have: initial first name + word middle name
    
    valid_name("H. George W.") ➞ False
    # Last name cannot be initial

### Notes

N/A

"""

def valid_name(name):
  lname = name.split(" ")
  
  if len(lname) == 2:
    if check_initial(lname[0]) and check_word(lname[1]):
      return True
    else:
      return False
  elif len(lname) == 3:
    if (check_initial(lname[0]) or check_word(lname[0])) and (check_initial(lname[1]) or (check_word(lname[1]) and not check_initial(lname[0]))) and (check_word(lname[2])):
      return True
    else:
      return False
  else:
    return False
    
def check_initial(string):
  if len(string) != 2:
    return False
  if not (65 <=ord(string[0]) and ord(string[0]) <= 90):
    return False
  if string[-1] != '.':
    return False
​
  return True
  
def check_word(string):
  if not len(string) > 2:
    return False
  if not (65 <=ord(string[0]) and ord(string[0]) <= 90):
    return False
  if '.' in string:
    return False
​
  return True

