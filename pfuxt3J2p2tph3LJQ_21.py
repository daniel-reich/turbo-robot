"""


Given a letter and a list of words, return whether the letter **does not
appear** in any of the words.

### Examples

    forbidden_letter("r", ["rock", "paper", "scissors"]) ➞ False
    
    forbidden_letter("a", ["spoon", "fork", "knife"]) ➞ True
    
    forbidden_letter("m", []) ➞ True

### Notes

  * All inputs given will be in lowercase.
  * You will always be given a **forbidden letter** , but there may be **empty lists**.

"""

def forbidden_letter(char, lst):
  return len([el for el in lst if el.count(char) == 0]) == len(lst)

