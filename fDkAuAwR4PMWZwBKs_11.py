"""


Write a function that searches a list of names (unsorted) for the name _"Bob"_
and returns the location in the list. If Bob is not in the list, return `-1`.

### Examples

    find_bob(["Jimmy", "Layla", "Bob"]) ➞ 2
    
    find_bob(["Bob", "Layla", "Kaitlyn", "Patricia"]) ➞ 0
    
    find_bob(["Jimmy", "Layla", "James"]) ➞ -1

### Notes

Assume all names start with a capital letter and are lowercase thereafter
(i.e. don't worry about finding "BOB" or "bob").

"""

def find_bob(names):
  try:
    return names.index("Bob")
  except:
    return -1

