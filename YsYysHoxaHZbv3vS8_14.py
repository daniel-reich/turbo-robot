"""


Given a set containing one element, return the element.

### Examples

    element_from_set({"edabit"}) ➞ "edabit"
    
    element_from_set({True}) ➞ True
    
    element_from_set({11037}) ➞ 11037

### Notes

Lists, dictionaries, and other sets won't be elements because sets won't
accept any mutable data types as elements.

"""

def element_from_set(s):
   for element in s:
      return element

