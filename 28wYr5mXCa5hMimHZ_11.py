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
    letters = []
    dot = 0
    for x in name:
        letters.append(x)
    count = 0
    for x in letters:
        if x == " ":
            count += 1
​
    print(count)
    if count == 0:
        return False
    if count > 2:
        return False
​
    first = 0
    second = 0
    third = 0
    for x in letters:
        print(x)
        if not(x == " "):
            first += 1
        else:
            break
    for x in letters[first+1:]:
​
        if not(x == " "):
            second += 1
        else:
            break
    for x in letters[first+second+2:]:
        third += 1
​
    print(first)
    print(second)
    print(third)
​
    if third < 3 and not(second > 0):
​
        return False
​
    if third == 0 and second < 3:
        return False
​
    if first < 3 and second >= 3 and not(third == 0):
        return  False
​
    if second == 0:
        return False
​
    if first == 1:
        return  False
​
    if second == 1:
        return False
​
    if third == 1:
        return False
​
    if str.isupper(letters[0]) == False:
        return False
    if str.isupper(letters[first + 1]) == False:
        return False
    if not(third==0):
        if str.isupper(letters[first+second+2]) == False:
            return False
​
​
    if not (third == 0):
        if first < 3 and second > 2:
            return False
    if letters[first-1] == "." and not (first == 2):
        return False
    if letters[first + second] == "." and not(second == 2):
        return False
    if letters[-1] == ".":
        return False
​
    return True

