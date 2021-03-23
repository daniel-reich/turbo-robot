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

def valid_name(s):
    if len(s.split())==3:
        a,b,c=s.split()
        if (len(a) == 2 and len(b)==2 and a.find('.')==1 and b.find('.')==1)\
        or (len(a) > 2 and len(b)==2 and b.find('.')==1 and a[0].isupper())\
        or (len(a) > 2 and len(b) > 2 and b.find('.') !=1 and a.find('.') != 1)\
        and a[0].isupper() and b[0].isupper() and c[0].isupper() and len(c) > 1 and c.find('.') !=1 :
            return True
        else:
            return False
    elif len(s.split())==2:
        a,c=s.split()
        if a.find('.')==1 and a[0].isupper() and c[0].isupper() and len(c) > 2:
            return True
        else:
            return False
    else:
        return False

