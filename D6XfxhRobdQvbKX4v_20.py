"""


You are given three inputs: a string, one letter, and a second letter.

Write a function that returns `True` if every instance of the first letter
occurs **before** every instance of the second letter.

### Examples

    first_before_second("a rabbit jumps joyfully", "a", "j") ➞ True
    # Every instance of "a" occurs before every instance of "j".
    
    first_before_second("knaves knew about waterfalls", "k", "w") ➞  True
    
    first_before_second("happy birthday", "a", "y") ➞ False
    # The "a" in "birthday" occurs after the "y" in "happy".
    
    first_before_second("precarious kangaroos", "k", "a") ➞ False

### Notes

  * All strings will be in lower case.
  * All strings will contain the first and second letters at least **once**.

"""

def first_before_second(s, first, second):
  found_first= False
  found_second = False
  for letter in s:
    if not found_first:
      if letter == second:
        return False
      if(letter == first):
        found_first= True
    else:
      if not found_second:
        if(letter == second):
          found_second = True
      else:
        if(letter== first):
          return False;
  return True

