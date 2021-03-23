"""


Create a function that takes a string and changes the word **amazing** to
**not amazing**. Return the string without any change if the word **edabit**
is part of the string.

### Examples

    amazing_edabit("edabit is amazing.") ➞ "edabit is amazing."
    
    amazing_edabit("Mubashir is amazing.") ➞ "Mubashir is not amazing."
    
    amazing_edabit("Infinity is amazing.") ➞ "Infinity is not amazing."

### Notes

Edabit is amazing :)

"""

def amazing_edabit(s):
  return s if "edabit" in s else s.split()[0] + " is not amazing."

