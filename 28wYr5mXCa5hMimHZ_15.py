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
  k = name.split(" ")
  if len(k) in (2,3) and '.' not in k[-1]:
    for i in k:
      if i[0].isupper():
        continue
      else:
        return False
        break
    else:
      if "." not in k[0] and '.' not in k[1] and len(k[0])!=1 and len(k[1])!=1:
        return True
      elif "." in k[1] and len(k[1])==2 and '.' not in k[0] and len(k[0])!=1:
        return True
      elif "." in k[0] and len(k[0])==2 and k[1]==k[-1]:
        return True
      elif "." in k[0] and '.' in k[1] and len(k[0])==2 and len(k[1])==2:
        return True 
      else:
        return False
  else:
    return False
