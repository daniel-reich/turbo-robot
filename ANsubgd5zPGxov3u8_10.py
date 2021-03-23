"""


Create a function that takes in a list of full names and returns the initials.

### Examples

    initialize(["Stephen Hawking"]) ➞ ["S. H."]
    
    initialize(["Harry Potter", "Ron Weasley"]) ➞ ["H. P.", "R. W."]
    
    initialize(["Sherlock Holmes", "John Watson", "Irene Adler"]) ➞ ["S. H.", "J. W.", "I. A."]

### Notes

  * Each initial is followed by a dot.
  * Names will always be made of two words, separated by a space.

"""

def initialize(names):
  ret = []
  for i in names:
    s = i.split()
    ret.append('{}. {}.'.format(s[0][0], s[1][0]))
  
  return ret

