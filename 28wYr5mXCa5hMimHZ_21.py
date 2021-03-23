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
    # count is word counter
    count = len(name.split())
    # storage for words
    flag = ""
    s1 = ""
    s2 = ""
    s3 = ""
    if count > 3 or count < 2:
        return False
    # splitting words to be analized individualy
    s1 = name.split()[0]
    s2 = name.split()[1]
    # checks is word is initial and if so one
    def initial_check(inp):
        if(len(inp)) == 2:
            if(inp[0].isupper()):
                if(inp[1] != '.'):
                   return False
                else:
                    return True
            else:
                return False
    # checks is word is name and if so one
    def name_check(inp):
        if(len(inp)) > 2:
            if(inp[0].isupper()):
                return True
            else:
                return False
        else:
            return False
    # 2 words check
    if count == 2:
        if(initial_check(s1)):
            flag += "i"
        if(name_check(s1)):
            flag += "n"
        if(initial_check(s2)):
            flag += "i"
        if(name_check(s2)):
            flag += "n"
    if(flag) == "in":
        return True
    elif(count == 2):
        return False
​
    # 3 words check
    if count == 3:
        s3 = name.split()[2]
        if(initial_check(s1)):
            flag += "i"
        if(name_check(s1)):
            flag += "n"
        if(initial_check(s2)):
            flag += "i"
        if(name_check(s2)):
            flag += "n"
        if(initial_check(s3)):
            flag += "i"
        if(name_check(s3)):
            flag += "n"
​
    if(flag == "nin" or flag == "nnn" or flag == "iin"):
        return True
    elif(count == 3):
        return False

